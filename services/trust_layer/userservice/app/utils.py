import json
import hashlib
import jwt
from pathlib import Path
from cryptography.fernet import Fernet
from app.config import settings
from passlib.context import CryptContext
from datetime import datetime, timedelta


fernet = Fernet(settings.ENCRYPTION_SECRET.encode())
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt_data(plaintext: str) -> str:
    return fernet.encrypt(plaintext.encode()).decode()

def decrypt_data(ciphertext: str) -> str:
    return fernet.decrypt(ciphertext.encode()).decode()

def load_metadata(path: Path = None, required_keys=None) -> dict:
    if path is None:
        path = Path(__file__).resolve().parent.parent / "metadata.json"

    if not path.exists():
        raise FileNotFoundError(f"metadata.json not found at: {path}")
    
    try:
        with path.open("r", encoding="utf-8") as f:
            metadata = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"metadata.json is not valid JSON: {e}")
    
    if required_keys:
        missing = [key for key in required_keys if key not in metadata]
        if missing:
            raise KeyError(f"metadata.json is missing required keys: {missing}")
        
    return metadata

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_email(email: str) -> str:
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()

def create_access_token(data: dict, expires_delta: int=None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def create_refresh_token(data: dict, expires_days: int=7) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=expires_days)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
