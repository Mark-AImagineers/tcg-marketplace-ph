from fastapi import FastAPI
from pathlib import Path
from .utils import load_metadata

from app.users.routes import router as user_router

REQUIRED_KEYS = [
    "service",
    "title",
    "version",
    "description",
    "status"
    ]

metadata = load_metadata()

app = FastAPI(
    title=metadata["title"],
    version=metadata["version"],
    description=metadata["description"],
)

@app.get("/")
async def root():
    return {
        "service": metadata["service"],
        "status": metadata["status"],
        "message": "User service running"
    }

@app.get("/status")
async def status():
    return metadata

app.include_router(user_router, prefix="/api/users")