from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.user import RegisterRequest, UserResponse
from app.models.user import User
from app.db import get_db
from app.utils import hash_password, hash_email

router = APIRouter()

### POST:/register ###
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(payload: RegisterRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email_hash == hash_email(payload.email)))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(payload.password)

    user = User(email=payload.email, hashed_password=hashed_pw)

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user

