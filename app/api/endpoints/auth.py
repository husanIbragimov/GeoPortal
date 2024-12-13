from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.api.auth.authentication import create_access_token, get_current_user
from app.core.utils import hash_password, verify_password
from app.models import User
from app.schemas.auth import UserRegister, UserLogin, UserResponse
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import status


router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/register", response_model=UserRegister)
async def register(user_create: UserRegister, db: Session = Depends(get_db)):
    # Check if username or email already exists
    db_user = db.query(User).filter((User.username == user_create.username) | (User.email == user_create.email)).first()
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
    

@router.post("/login", response_model=UserLogin)
async def login(user_login: UserLogin, db: Session = Depends(get_db)):
    # Fetch user from DB
    db_user = db.query(User).filter(User.username == user_login.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(user_login.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Create JWT token
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/logout")
async def logout():
    # In FastAPI, logout usually involves removing the access token on the client-side.
    return {"message": "Successfully logged out"}

