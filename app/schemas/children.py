from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class ChildBase(BaseModel):
    difficulty: str
    name: Optional[str]
    birth_date: Optional[date]

class ChildCreate(ChildBase):
    pass #pass? or name + birthdate?

class Child(ChildBase):
    child_id: int
    user_id: int
    name: Optional[str]
    birth_date: date
    created_at: datetime

    class Config:
        from_attributes = True

class ChildUpdate(BaseModel):
    name: Optional[str]
    difficulty: Optional[str]
    birth_date: Optional[date]

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
