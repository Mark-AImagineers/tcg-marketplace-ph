import csv
import os
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.cards import Card

DUMP_PATH = "/app/data/all_cards_dump.csv"

def dump_all_cards_to_csv():
    db: Session = SessionLocal()
    cards = db.query(Card).all()
    db.close()

    if not cards:
        print("⚠️ No cards found in DB.")
        return

    os.makedirs(os.path.dirname(DUMP_PATH), exist_ok=True)

    with open(DUMP_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "name", "set", "series", "release_date", "types", "supertype",
            "subtypes", "hp", "evolves_from", "attacks", "rarity",
            "retreat_cost", "flavor_text"
        ])
        writer.writeheader()

        for card in cards:
            writer.writerow({
                "id": card.id,
                "name": card.name,
                "set": card.set,
                "series": card.series,
                "release_date": card.release_date,
                "types": card.types,
                "supertype": card.supertype,
                "subtypes": card.subtypes,
                "hp": card.hp,
                "evolves_from": card.evolves_from,
                "attacks": card.attacks,
                "rarity": card.rarity,
                "retreat_cost": card.retreat_cost,
                "flavor_text": card.flavor_text,
            })

    print(f"✅ Dumped {len(cards)} cards to {DUMP_PATH}")
