# fastapi
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme
from app.schemas.children import Child, ChildCreate, ChildUpdate
from app.api.endpoints.children import functions as child_functions

child_module = APIRouter()


# @user_module.get('/')
# async def read_auth_page():
#     return {"msg": "Auth page Initialization done"}

# create new user
@child_module.post('/', response_model=Child)
async def create_new_child(child: ChildCreate, db: Session = Depends(get_db)):
    db_child = child_functions.get_child_by_name(db, child.name)
    if db_child:
        raise HTTPException(status_code=400, detail="User already exists")
    new_child = child_functions.create_new_child(db, child)
    return new_child

# get all user
@child_module.get('/',
            response_model=list[Child],
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_children( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return child_functions.read_all_user(db, skip, limit)

# get user by id
@child_module.get('/{child_id}',
            response_model=Child,
            # dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_user_by_id( child_id: int, db: Session = Depends(get_db)):
    return child_functions.get_child_by_id(db, child_id)

# update user
@child_module.patch('/{child_id}',
              response_model=Child,
            #   dependencies=[Depends(RoleChecker(['admin']))]
              )
async def update_child( child_id: int, child: ChildUpdate, db: Session = Depends(get_db)):
    print(f"Received data: {child.model_dump()}")
    return child_functions.update_user(db, child_id, child)

# delete user
@child_module.delete('/{child_id}',
            #    response_model=Child,
            #    dependencies=[Depends(RoleChecker(['admin']))]
               )
async def delete_child( child_id: int, db: Session = Depends(get_db)):
    return child_functions.delete_child(db, child_id)


