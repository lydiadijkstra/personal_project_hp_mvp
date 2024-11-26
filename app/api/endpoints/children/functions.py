from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# from auth import models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

# import
from app.models import user as ChildModel
from app.schemas.children import ChildCreate, ChildUpdate, Token
from app.core.settings import SECRET_KEY, REFRESH_SECRET_KEY, ALGORITHM
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.dependencies import get_db, oauth2_scheme

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# get user by email
def get_child_by_name(db: Session, name: str):
    return db.query(ChildModel.Child).filter(ChildModel.Child.name == name).first()


# get user by id
def get_child_by_id(db: Session, child_id: int):
    db_child = db.query(ChildModel.User).filter(ChildModel.Child.child_id == child_id).first()
    if db_child is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_child


# crete new user
def create_new_child(db: Session, child: ChildCreate):
    hashed_password = pwd_context.hash(child.password)
    new_child = ChildModel.Child(child_name=child.child_name, location=child.location, email=child.email,
                              password=hashed_password, name=child.name,
                              role=child.role if child.role else 'child')  # Default to 'child' if not provided)
    db.add(new_child)
    db.commit()
    db.refresh(new_child)
    return new_child


# get all user
def read_all_children(db: Session, skip: int, limit: int):
    return db.query(ChildModel.Child).offset(skip).limit(limit).all()


# update user
def update_child(db: Session, child_id: int, child: ChildUpdate):
    db_child = get_child_by_id(db, child_id)
    updated_data = child.model_dump(exclude_unset=True)  # partial update
    for key, value in updated_data.items():
        setattr(db_child, key, value)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child


# delete user
def delete_child(db: Session, child_id: int):
    db_child = get_child_by_id(db, child_id)
    db.delete(db_child)
    db.commit()
    db.refresh(db_child)
    return {"msg": f"{db_child.name} deleted successfully"}


# =====================> login/logout <============================
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, user: UserCreate):
    member = get_user_by_email(db, user.email)
    if not member:
        return False
    if not verify_password(user.password, member.password):
        return False
    return member


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def refresh_access_token(db: Session, refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        # member = await User.get(user_id)
        member = get_user_by_id(db, user_id)
        if member is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"user_id": member.user_id, "email": member.email, "role": member.role},
            expires_delta=access_token_expires
        )
        return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


# get current users info
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(f"Payload =====> {payload}")
        current_email: str = payload.get("email")
        if current_email is None:
            raise credentials_exception
        user = get_user_by_email(db, current_email)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception

