import csv
import json
from sqlalchemy.exc import IntegrityError
from app.db import SessionLocal
from app.models.cards import Card

CSV_PATH = "data/cards.csv"

def parse_list(raw):
    try:
        return json.loads(raw.replace("'", '"'))
    except Exception:
        return None

def main():
    db = SessionLocal()

    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            card = Card(
                id=row["id"],
                name=row["name"],
                set=row["set"],
                series=row["series"],
                release_date=row["release_date"],
                types=parse_list(row["types"]),
                supertype=row["supertype"],
                subtypes=parse_list(row["subtypes"]),
                hp=int(row["hp"]) if row["hp"].isdigit() else None,
                evolves_from=row.get("evolvesFrom"),
                attacks=parse_list(row["attacks"]),
                rarity=row["rarity"],
                retreat_cost=parse_list(row["retreatCost"]),
                flavor_text=row.get("flavorText"),
            )

            try:
                db.add(card)
                db.commit()
            except IntegrityError:
                db.rollback()
                print(f"Skipping duplicate: {card.id}")
        
    db.close()

if __name__ == "__main__":
    main() 