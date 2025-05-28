from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
import json

from app.sync.checker import get_missing_card_ids
from app.sync.puller import pull_cards_from_ids
from app.sync.dump import dump_all_cards_to_csv

router = APIRouter(prefix="/sync", tags=["sync"])


@router.get("/check")
def check_missing_cards(api_key: str = Query(..., description="PokéTCG.io API key")):
    try:
        missing = get_missing_card_ids(api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sync check failed: {str(e)}")

    return {
        "missing_count": len(missing),
        "message": f"🟢 Saved {len(missing)} missing IDs to /DATA"
    }


@router.get("/pull")
def pull_missing_cards(api_key: str = Query(..., description="PokéTCG.io API key")):
    missing_path = Path("/app/data/missing_ids.json")
    if not missing_path.exists():
        raise HTTPException(status_code=404, detail="Missing ID file not found")

    try:
        with open(missing_path) as f:
            missing_ids = json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read missing ID file: {str(e)}")

    if not isinstance(missing_ids, list) or not missing_ids:
        return {
            "status": "no-op",
            "message": "No missing cards to pull",
            "fetched_count": 0
        }

    try:
        results = pull_cards_from_ids(missing_ids, api_key=api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pull failed: {str(e)}")

    return {
        "status": "ok",
        "fetched_count": len(results),
        "message": f"🟢 Pulled {len(results)} cards successfully",
        "sample": results[:3]
    }

@router.get("/dump")
def dump_card_data():
    try:
        dump_all_cards_to_csv()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dump failed: {str(e)}")

    return {
        "message": "✅ Card data dumped to CSV successfully.",
        "filename": "all_cards_dump.csv"
    }