# fastapi
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme
from app.schemas.children import Child, ChildCreate, ChildUpdate
from app.models.children import Child as ChildModel
from app.api.endpoints.children import functions as child_functions
from app.api.endpoints.user.functions import get_current_user
from app.schemas.user import User


child_module = APIRouter()


@child_module.post('/', response_model=Child)
async def create_new_child(
    child: ChildCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if a child with the same name exists
    db_child = db.query(ChildModel).filter_by(name=child.name, user_id=current_user.user_id).first()
    if db_child:
        raise HTTPException(status_code=400, detail="You have already entered a child with this name.")

    # Create the new child instance
    new_child = ChildModel(
        name=child.name,
        difficulty=child.difficulty,
        birth_date=child.birth_date,
        user_id=current_user.user_id,
    )

    # Add the new child-date to the Database
    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    return new_child


# get all children
@child_module.get('/', response_model=list[Child])
async def read_all_children(skip: int = 0, limit: int = 100,  db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return child_functions.read_all_children(db, current_user, skip, limit)


# get child by id
@child_module.get('/{child_id}', response_model=Child)
async def read_child_by_id(child_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return child_functions.get_child_by_id(db, child_id, current_user)


# get child by name
@child_module.get('/name/{name}', response_model=Child)
async def read_child_by_name(name: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return child_functions.get_child_by_name(db, name, current_user)


# update child
@child_module.patch('/{child_id}', response_model=Child)
async def update_child(child_id: int, child: ChildUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    print(f"Received data: {child.model_dump()}")
    return child_functions.update_child(db, child_id, child, current_user)


# delete child
@child_module.delete('/{child_id}')
async def delete_child( child_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return child_functions.delete_child(db, child_id, current_user)
