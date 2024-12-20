"""
from fastapi import APIRouter, HTTPException
from app.schemas.tips import Tip  # Assuming Tip is your SQLAlchemy model mapped to the DB


router = APIRouter()


@router.get("/tips/{tip_id}", response_model=Tip)
async def get_tip(tip_id: int):
    # Query your database for the tip with the given ID
    tip = db.query(Tip).filter(Tip.tip_id == tip_id).first()  # assuming 'db' is your DB session
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")
    return tip

"""
# fastapi
from alembic.command import current
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user

# import
from app.core.dependencies import get_db, oauth2_scheme
from app.schemas.tips import Tip, TipCreate
from app.models.tips import Tip as TipModel
from app.models.children import Child as ChildModel
from app.api.endpoints.tips import functions as tip_functions
from app.api.endpoints.user.functions import get_current_user
from app.api.endpoints.children.functions import (create_new_child, read_all_children, update_child, delete_child)
from app.schemas.user import User


tip_module = APIRouter()


# get all tips
@tip_module.get('/', response_model=list[Tip])
async def read_all_tips(skip: int = 0, limit: int = 100,  db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return tip_functions.read_all_tips(db, current_user, skip, limit)


# get tip by id
@tip_module.get('/{tip_id}', response_model=Tip,
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_tip_by_id(tip_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return tip_functions.get_tip_by_id(db, tip_id, current_user)


#create tip
@tip_module.post('/create/{child_id}', response_model=Tip)
async def create_tip_endpoint(
    child_id: int,
    tip: TipCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return tip_functions.create_new_tip(db, tip, current_user, child_id)
