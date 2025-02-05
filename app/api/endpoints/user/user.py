# fastapi
from fastapi import APIRouter, Depends, HTTPException

# sqlalchemy
from sqlalchemy.orm import Session

# import
from app.core.dependencies import get_db, oauth2_scheme
from app.schemas.user import User, UserCreate, UserUpdate
from app.api.endpoints.user import functions as user_functions
from app.api.endpoints.user.functions import get_current_user


user_module = APIRouter()


# create new user 
@user_module.post('/', response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_functions.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = user_functions.create_new_user(db, user)
    return new_user


# get all user 
@user_module.get('/', 
            response_model=list[User])
async def read_all_user( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return user_functions.read_all_user(db, skip, limit)


# get user by id 
@user_module.get('/{user_id}', 
            response_model=User)
async def read_user_by_id( user_id: int, db: Session = Depends(get_db)):
    return user_functions.get_user_by_id(db, user_id)


# get user by email
@user_module.get('/email/{email}',
            response_model=User)
async def read_user_by_email( email: str, db: Session = Depends(get_db)):
    return user_functions.get_user_by_email(db, email)


# update user
@user_module.patch('/{user_id}', 
              response_model=User)
async def update_user( user_id: int, user: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    print(f"Received data: {user.model_dump()}")
    return user_functions.update_user(db, user_id, user, current_user)


# delete user
@user_module.delete('/{user_id}')
async def delete_user( user_id: int, db: Session = Depends(get_db)):
    return user_functions.delete_user(db, user_id)
