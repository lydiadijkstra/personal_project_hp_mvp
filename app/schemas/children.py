from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class ChildBase(BaseModel):
    difficulty: str
    name: str
    birth_date: date


class ChildCreate(ChildBase):
    pass


class Child(ChildBase):
    child_id: int = Field(..., description="Unique ID for the child")
    user_id: int = Field(..., description="ID of the user who created the child")
    created_at: datetime = Field(..., description="Timestamp when the child record was created")

    class Config:
        orm_mode = True  # Ensure compatibility with SQLAlchemy models


class ChildUpdate(BaseModel):
    name: Optional[str]
    difficulty: Optional[str]
    birth_date: Optional[date]
