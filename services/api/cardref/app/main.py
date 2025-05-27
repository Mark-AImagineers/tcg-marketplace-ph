from fastapi import FastAPI
from app.db import engine, Base
from app.models import cards
from app.api.routes import sync

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(sync.router)

@app.get("/")
def read_root():
    return {"message": "Red, Card Reference API is live"}

