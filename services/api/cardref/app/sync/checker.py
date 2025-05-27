import requests
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.cards import Card

def get_poketcg_card_ids(api_key: str) -> set[str]:
    url = "https://api.pokemontcg.io/v2/cards"
    headers = {"X-Api-Key": api_key}
    page = 1
    page_size = 250
    all_ids = set()

    while True:
        response = requests.get(
            url, headers=headers, params={"page": page, "pageSize": page_size}
        )
        data = response.json()
        cards = data.get("data", [])
        if not cards:
            break

        print(f"✅ Fetched page {page} with {len(cards)} cards")
        for card in cards:
            all_ids.add(card["id"])

        page += 1

    return all_ids

def get_local_card_ids() -> set[str]:
    db: Session = SessionLocal()
    result = db.query(Card.id).all()
    db.close()
    return set(row[0] for row in result)

def get_missing_card_ids(api_key: str) -> set[str]:
    remote_ids = get_poketcg_card_ids(api_key)
    local_ids = get_local_card_ids()
    return remote_ids - local_ids

