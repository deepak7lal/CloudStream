from fastapi import APIRouter

router = APIRouter(prefix="/videos", tags=["Videos"])

videos = [
    {
        "id": 1,
        "title": "Kubernetes Basics",
        "duration": "10:12"
    },
    {
        "id": 2,
        "title": "Docker Crash Course",
        "duration": "18:40"
    }
]

@router.get("/")
def get_videos():
    return videos