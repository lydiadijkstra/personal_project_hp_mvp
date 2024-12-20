from alembic.command import current
from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

# import
from app.models import user as UserModel
from app.models.children import Child as ChildModel
from app.models.tips import Tip as TipModel
from app.schemas.tips import Tip, TipCreate
from app.api.endpoints.user.functions import get_current_user
from app.core.gemini_api_datafetcher import get_ai_tip


# Resolve forward references
TipCreate.model_rebuild()


# create new tip
def create_new_tip(db: Session, tip: TipCreate, current_user: UserModel.User, child_id: int):
    try:
        # Validate that the child exists for the current user
        child = db.query(ChildModel).filter(
            ChildModel.child_id == child_id,
            ChildModel.user_id == current_user.user_id
        ).first()
        if not child:
            raise HTTPException(status_code=404, detail="Child not found or not authorized to access")

        problem_type = child.difficulty
        tip_content = get_ai_tip(problem_type=problem_type)
    except Exception as e:
        print(f"Error generating tip: {e}")
        raise HTTPException(status_code=500, detail="Error generating tip")

    # create the new tip
    new_tip = TipModel(
        user_id=current_user.user_id,
        child_id=child.child_id,
        problem_type=tip.problem_type,
        content=tip_content
    )
    print(tip_content)
    db.add(new_tip)
    db.commit()
    db.refresh(new_tip)

    return new_tip


# get all tips
def read_all_tips(db: Session, current_user: Annotated[UserModel.User, Depends(get_current_user)], skip: int = 0, limit: int = 10):
    return db.query(TipModel).filter(TipModel.user_id == current_user.user_id).offset(skip).limit(limit).all()


# Get a specific tip by ID, ensuring it belongs to the logged-in user
def get_tip_by_id(db: Session, tip_id: int, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    db_tip = db.query(TipModel).filter(
        TipModel.tip_id == tip_id,
        TipModel.user_id == current_user.user_id,  # Ensures the tip belongs to the user
    ).first()
    if db_tip is None:
        raise HTTPException(status_code=404, detail="Tip not found or not authorized to access")
    return db_tip
