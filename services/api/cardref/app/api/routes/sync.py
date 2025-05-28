from fastapi import APIRouter, Query, HTTPException
from app.sync.checker import get_missing_card_ids

router = APIRouter(prefix="/sync", tags=["sync"])

@router.get("/check")
def check_missing_cards(api_key: str = Query(..., description="PokéTCG.io API key")):
    try:
        missing = get_missing_card_ids(api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sync check failed: {str(e)}")

    return {
        "missing_count": len(missing),
        "missing_ids": list(missing)[:10]
    }
