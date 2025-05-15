from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
from app.utils import encrypt_data, decrypt_data, hash_email

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    _email = Column("email", String, unique=True, index=True, nullable=False)
    email_hash = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @property
    def email(self) -> str:
        return decrypt_data(self._email)
    
    @email.setter
    def email(self, value: str):
        self._email = encrypt_data(value)
        self.email_hash = hash_email(value)