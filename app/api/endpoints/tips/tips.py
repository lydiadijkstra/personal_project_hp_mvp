# fastapi
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme
from app.schemas.tips import Tip, TipCreate
from app.api.endpoints.tips import functions as tip_functions
from app.api.endpoints.user.functions import get_current_user
from app.schemas.user import User


tip_module = APIRouter()


# get all tips
@tip_module.get('/', response_model=list[Tip])
async def read_all_tips(skip: int = 0, limit: int = 100,  db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return tip_functions.read_all_tips(db, current_user, skip, limit)


# get tip by id
@tip_module.get('/{tip_id}', response_model=Tip)
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
