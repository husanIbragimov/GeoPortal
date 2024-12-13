import random
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    username: str
    password: str
    password2: str
    email: EmailStr
    full_name: str
    gender: Optional[str] = random.choice(["Male", "Female"])

    class Config:
        from_attributes = True
    
    def validate(self):
        if self.password != self.password2:
            raise ValueError("Password and Confirm Password must match")
        return self

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    full_name: str
    gender: str
    is_active: bool

    class Config:
        from_attributes = True
