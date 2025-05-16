from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.user import RegisterRequest, UserResponse
from app.models.user import User
from app.db import get_db
from app.utils import hash_password, hash_email, verify_password, create_access_token, create_refresh_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Form, Header, Security, HTTPException, status, Depends

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired access token")
    return payload["sub"]
    

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


### POST:/login ###
@router.post("/login")
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession= Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email_hash == hash_email(form_data.username))
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

### POST:/refresh ###
@router.post("/refresh")
async def refresh_token(refresh_token: str = Header(...)):
    payload = decode_token(refresh_token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = create_access_token(data={"sub": payload["sub"]})
    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }

### GET:/me ###
@router.get("/me")
async def get_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}