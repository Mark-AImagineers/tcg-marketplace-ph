from fastapi import FastAPI
from app.db import engine, Base
from app.models import cards

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Red, Card Reference API is live"}

