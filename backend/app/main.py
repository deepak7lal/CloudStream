from fastapi import FastAPI
from app.routers import files

from app.routers import auth
from app.database import Base, engine

# Import models so SQLAlchemy knows about them
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudStream API",
    version="1.0.0"
)
app.include_router(files.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to CloudStream API 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }