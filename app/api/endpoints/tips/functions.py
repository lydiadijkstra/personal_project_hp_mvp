from alembic.command import current
from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# from auth import models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

# import
from app.models import user as UserModel
from app.models import tips as TipModel
from app.schemas.tips import TipCreate, TipUpdate#, Token
from app.core.settings import SECRET_KEY, REFRESH_SECRET_KEY, ALGORITHM
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.dependencies import get_db, oauth2_scheme
from app.api.endpoints.user.functions import get_current_user


# Resolve forward references
TipCreate.model_rebuild()
TipUpdate.model_rebuild()


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# create new tip
def create_new_tip(db: Session, tip: TipCreate, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    new_tip = TipModel.Tip(
        content=tip.content,
        problem_type=tip.problem_type,
        created_by=current_user.user_name
    )
    db.add(new_tip)
    db.commit()
    db.refresh(new_tip)
    return new_tip

"""
    tip_id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    problem_type = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)
"""

# get all tips
def read_all_tips(db: Session, current_user: Annotated[UserModel.User, Depends(get_current_user)], skip: int = 0, limit: int = 10):
    return db.query(TipModel.Tip).filter(TipModel.Tip.user_id == current_user.user_id).offset(skip).limit(limit).all()


# Get a specific tip by ID, ensuring it belongs to the logged-in user
def get_tip_by_id(db: Session, tip_id: int, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_tip = db.query(TipModel.Tip).filter(
        TipModel.Tip.tip_id == tip_id,
        TipModel.Tip.user_id == current_user.user_id,  # Ensures the tip belongs to the user
    ).first()
    if db_tip is None:
        raise HTTPException(status_code=404, detail="Child not found or not authorized to access")
    return db_tip


# Get a specific tip by content, ensuring it belongs to the logged-in user
def get_tip_by_content(db: Session, content: str, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_tip = db.query(TipModel.Tip).filter(
        TipModel.Tip.content == content,
        TipModel.Tip.user_id == current_user.user_id,  # Ensure the child belongs to the user
    ).first()
    if db_tip is None:
        raise HTTPException(status_code=404, detail="Child not found or not authorized to access")
    return db_tip


# update child, ensuring it belongs to logged-in user
def update_tip(db: Session, tip_id: int, tip: TipUpdate, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_tip = get_tip_by_id(db, tip_id, current_user)
    updated_data = tip.model_dump(exclude_unset=True)  # partial update
    for key, value in updated_data.items():
        setattr(db_tip, key, value)
    db.add(db_tip)
    db.commit()
    db.refresh(db_tip)
    return db_tip


# delete tip, ensuring the child is connected to the active user
def delete_tip(db: Session, tip_id: int, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_tip= get_tip_by_id(db, tip_id, current_user)
    db.delete(db_tip)
    db.commit()
    # db.refresh(db_child) # child no longer in the database, so refresh the child is not possible -> internal server error
    return {"msg": f"{db_tip.content} deleted successfully"}

