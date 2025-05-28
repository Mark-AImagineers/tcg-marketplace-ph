import json
import time
import requests
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.cards import Card

DATA_PATH = "/app/data/missing_ids.json"
DAILY_LIMIT = 20000
SAFE_LIMIT = int(DAILY_LIMIT * 0.8)

def pull_cards_by_ids(api_key: str):
    with open(DATA_PATH, encoding="utf-8") as f:
        all_ids = json.load(f)

    if len(all_ids) > SAFE_LIMIT:
        print(f"⚠️ {len(all_ids)} cards listed — only processing first {SAFE_LIMIT} to respect rate limits")
        ids_to_process = all_ids[:SAFE_LIMIT]
    else:
        ids_to_process = all_ids

    db: Session = SessionLocal()
    headers = {"X-Api-Key": api_key}
    base_url = "https://api.pokemontcg.io/v2/cards"

    for i, card_id in enumerate(ids_to_process):
        url = f"{base_url}/{card_id}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"❌ Failed to fetch {card_id}: {response.status_code}")
            continue

        card_data = response.json().get("data", {})
        
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
        print(f"✅ Inserted {card.id} ({i+1}/{len(ids_to_process)})")

        #Rate limit safety buffer
        time.sleep(0.6)

    db.close()

    if len(all_ids) > SAFE_LIMIT:
        print(f"\n⚠️ Pull limited to {SAFE_LIMIT} cards. {len(all_ids) - SAFE_LIMIT} skipped.")
        print("📎 Rerun tomorrow or split pulls to cover the rest.")
