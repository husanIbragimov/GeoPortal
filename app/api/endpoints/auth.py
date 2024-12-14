from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.api.auth.authentication import tokens, get_current_user
from app.core.utils import hash_password, verify_password
from app.models import User
from app.schemas.auth import UserRegister, UserLogin, UserSchema, TokenSchema
from . import get_db

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register/", response_model=UserRegister, status_code=status.HTTP_201_CREATED)
async def register(user_create: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered")

    hashed_password = hash_password(user_create.password)
    new_user = User(
        username=user_create.username,
        email=user_create.email,
        full_name=user_create.full_name,
        gender=user_create.gender,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login/", response_model=TokenSchema)
async def login(
    db: Session = Depends(get_db),
    form_data: UserLogin = Depends()
):
    db_user = db.query(User).filter(User.username == form_data.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return tokens(data={"sub": db_user.username})


@router.get("/user/me", response_model=UserSchema)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/logout/")
async def logout():
    # In FastAPI, logout usually involves removing the access token on the client-side.
    return {"message": "Successfully logged out"}
