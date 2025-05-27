from sqlalchemy import Column, String, JSON, Integer
from app.db import Base

class Card(Base):
    __tablename__="cards"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    set = Column(String)
    series = Column(String)
    release_date = Column(String)
    types = Column(JSON, nullable=True)
    supertype = Column(String, nullable=True)
    subtypes = Column(JSON, nullable=True)
    hp = Column(Integer, nullable=True)
    evolves_from = Column(String, nullable=True)
    attacks = Column(JSON, nullable=True)
    rarity = Column(String, nullable=True)
    retreat_cost = Column(JSON, nullable=True)
    flavor_text = Column(String, nullable=True)
    




