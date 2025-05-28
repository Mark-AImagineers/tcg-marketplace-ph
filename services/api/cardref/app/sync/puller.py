import json
import time
import os
import requests
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.cards import Card

DATA_PATH = "/app/data/missing_ids.json"
DAILY_LIMIT = 20000
SAFE_LIMIT = int(DAILY_LIMIT * 0.8)
RATE_LIMIT_DELAY = 0.6  # seconds

# ✅ Core reusable function (used by CLI + API)
def pull_cards_from_ids(card_ids: list, api_key: str):
    db: Session = SessionLocal()
    headers = {"X-Api-Key": api_key}
    base_url = "https://api.pokemontcg.io/v2/cards"
    results = []

    for i, card_id in enumerate(card_ids):
        url = f"{base_url}/{card_id}"
        try:
            response = requests.get(url, headers=headers)
        except requests.RequestException as e:
            print(f"❌ Network error for {card_id}: {e}")
            continue

        if response.status_code != 200:
            print(f"❌ Failed to fetch {card_id}: {response.status_code}")
            continue

        card_data = response.json().get("data", {})
        if not card_data:
            print(f"❌ No data for {card_id}")
            continue

        if db.query(Card).filter_by(id=card_data["id"]).first():
            print(f"⏩ Skipped {card_data['id']} (already in DB)")
            continue

        card = Card(
            id=card_data["id"],
            name=card_data.get("name"),
            set=card_data.get("set", {}).get("name"),
            series=card_data.get("set", {}).get("series"),
            release_date=card_data.get("set", {}).get("releaseDate"),
            types=card_data.get("types"),
            supertype=card_data.get("supertype"),
            subtypes=card_data.get("subtypes"),
            hp=int(card_data.get("hp", 0)) if card_data.get("hp", "").isdigit() else None,
            evolves_from=card_data.get("evolvesFrom"),
            attacks=card_data.get("attacks"),
            rarity=card_data.get("rarity"),
            retreat_cost=card_data.get("retreatCost"),
            flavor_text=card_data.get("flavorText"),
        )

        db.add(card)
        db.commit()
        results.append(card.id)
        print(f"✅ Inserted {card.id} ({i+1}/{len(card_ids)})")
        time.sleep(RATE_LIMIT_DELAY)

    db.close()
    return results


# ✅ CLI-style wrapper (reads from file)
def pull_cards_by_ids(api_key: str):
    with open(DATA_PATH, encoding="utf-8") as f:
        all_ids = json.load(f)

    if len(all_ids) > SAFE_LIMIT:
        print(f"⚠️ {len(all_ids)} cards listed — processing only first {SAFE_LIMIT}")
        all_ids = all_ids[:SAFE_LIMIT]

    return pull_cards_from_ids(all_ids, api_key)
