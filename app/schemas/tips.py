from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class TipsBase(BaseModel):
    content: str
    problem_type: str
    created_by: str


class TipsCreate(TipsBase):
    pass


class Tips(TipsBase):
    tip_id: int = Field(..., description="Unique ID for the tip")
    problem_type: str = Field(..., description="Problemtype which the tip is created for")
    created_at: datetime = Field(..., description="Timestamp when the child record was created")

    class Config:
        from_attributes = True  # Ensure compatibility with SQLAlchemy models


class ChildUpdate(BaseModel):
    content: Optional[str]
    problem_type: Optional[str]
    created_by: Optional[date]
