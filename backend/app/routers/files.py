from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.database import get_db
from app.file_models import File as FileModel
from app.minio_client import client, BUCKET_NAME

import io

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    object_name = file.filename

    data = file.file.read()

    client.put_object(
        BUCKET_NAME,
        object_name,
        io.BytesIO(data),
        length=len(data),
        content_type=file.content_type
    )

    new_file = FileModel(
        filename=file.filename,
        object_name=object_name,
        uploaded_by=current_user
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {
        "message": "File uploaded successfully",
        "file_id": new_file.id,
        "filename": new_file.filename
    }


@router.get("/")
def list_files(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    files = db.query(FileModel).filter(
        FileModel.uploaded_by == current_user
    ).all()

    return files


@router.get("/{file_id}")
def download_file(
    file_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    file = db.query(FileModel).filter(
        FileModel.id == file_id,
        FileModel.uploaded_by == current_user
    ).first()

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    response = client.get_object(
        BUCKET_NAME,
        file.object_name
    )

    return StreamingResponse(
        response,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f'attachment; filename="{file.filename}"'
        }
    )


@router.delete("/{file_id}")
def delete_file(
    file_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    file = db.query(FileModel).filter(
        FileModel.id == file_id,
        FileModel.uploaded_by == current_user
    ).first()

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    client.remove_object(
        BUCKET_NAME,
        file.object_name
    )

    db.delete(file)
    db.commit()

    return {
        "message": "File deleted successfully"
    }