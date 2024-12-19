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
from app.models import children as ChildModel
from app.schemas.children import ChildCreate, ChildUpdate#, Token
from app.core.settings import SECRET_KEY, REFRESH_SECRET_KEY, ALGORITHM
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.dependencies import get_db, oauth2_scheme
from app.api.endpoints.user.functions import get_current_user
from app.core.gemini_api_datafetcher import get_ai_tip
from app.models.tips import Tip

#add logging for debugging the problem not getting a print and not creating a tip
import logging
logging.basicConfig(level=logging.DEBUG)


# Resolve forward references
ChildCreate.model_rebuild()
ChildUpdate.model_rebuild()


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# create new child
def create_new_child(db: Session, child: ChildCreate, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    #hashed_password = pwd_context.hash(child.password)
    new_child = ChildModel.Child(
        name=child.name,
        age=child.age,
        user_id=current_user.user_id
    )
    #print("new child creation starts here")
    #logging.debug("i will create a new child now ! / children_functions")

    #add try except for debugging the print problem
    try:
        logging.debug("I will create a new child now! / children_functions")
        ...
    except Exception as e:
        logging.debug(f"Error occurred: {e}")
        raise

    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    return new_child
"""
    logging.debug("this is the point where the child is created and creating the tip starts")
    # Create first tip for the issue the parent has
    logging.debug(f"Child difficulty: {child.difficulty}")
    try:
        tip_content = get_ai_tip(problem_type=child.difficulty)
        logging.debug("successfully created child and entered the try get ai tip / children functions")
    except Exception as e:
        logging.debug("Sorry yu could not leave the create child to go to generate tip / children functions")

        raise HTTPException(status_code=500, detail="Error generating tip")

        # Store the tip in the database
    new_tip = Tip(
        user_id=current_user.id,
        child_id=new_child.id,
        problem=child.difficulty,
        tip_content=tip_content
    )
    logging.debug(tip_content)
    db.add(new_tip)
    db.commit()
    db.refresh(new_tip)
"""



# get all children
def read_all_children(db: Session, current_user: Annotated[UserModel.User, Depends(get_current_user)], skip: int = 0, limit: int = 10):
    return db.query(ChildModel.Child).filter(ChildModel.Child.user_id == current_user.user_id).offset(skip).limit(limit).all()


# Get a specific child by ID, ensuring it belongs to the logged-in user
def get_child_by_id(db: Session, child_id: int, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_child = db.query(ChildModel.Child).filter(
        ChildModel.Child.child_id == child_id,
        ChildModel.Child.user_id == current_user.user_id,  # Ensures the child belongs to the user
    ).first()
    if db_child is None:
        raise HTTPException(status_code=404, detail="Child not found or not authorized to access")
    return db_child


# Get a specific child by ID, ensuring it belongs to the logged-in user
def get_child_by_name(db: Session, name: str, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_child = db.query(ChildModel.Child).filter(
        ChildModel.Child.name == name,
        ChildModel.Child.user_id == current_user.user_id,  # Ensure the child belongs to the user
    ).first()
    if db_child is None:
        raise HTTPException(status_code=404, detail="Child not found or not authorized to access")
    return db_child


# update child, ensuring it belongs to logged-in user
def update_child(db: Session, child_id: int, child: ChildUpdate, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_child = get_child_by_id(db, child_id, current_user)
    updated_data = child.model_dump(exclude_unset=True)  # partial update
    for key, value in updated_data.items():
        setattr(db_child, key, value)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child


# delete child, ensuring the child is connected to the active user
def delete_child(db: Session, child_id: int, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_child = get_child_by_id(db, child_id, current_user)
    db.delete(db_child)
    db.commit()
    # db.refresh(db_child) # child no longer in the database, so refresh the child is not possible -> internal server error
    return {"msg": f"{db_child.name} deleted successfully"}

