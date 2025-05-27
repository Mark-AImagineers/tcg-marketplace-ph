from fastapi import APIRouter

router = APIRouter(prefix="/sync", tags=["sync"])

@router.get("/check")
def check_missing_cards():
    return {"message": "Sync check endpoint working"}