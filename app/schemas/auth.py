import random
from typing import Optional

from app.models import GenderEnum
from pydantic import BaseModel, EmailStr, validator


class UserRegister(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str
    gender: Optional[GenderEnum] = GenderEnum.male

    class Config:
        from_attributes = True

    @validator('gender', pre=True, always=True)
    def validate_gender(cls, v):
        if isinstance(v, str):
            v = v.lower()  # Normalize to lowercase
        return GenderEnum(v)


class TokenSchema(BaseModel):
    refresh: str
    access: str
    token_type: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    uuid: str
    username: str
    email: EmailStr
    full_name: str
    gender: str
    is_active: bool

    class Config:
        from_attributes = True
