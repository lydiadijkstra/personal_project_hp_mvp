from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class TipBase(BaseModel):
    content: str
    problem_type: str
    created_by: str


class TipCreate(TipBase):
    pass


class Tip(TipBase):
    tip_id: int = Field(..., description="Unique ID for the tip")
    problem_type: str = Field(..., description="Problemtype which the tip is created for")
    created_at: datetime = Field(..., description="Timestamp when the child record was created")

    class Config:
        from_attributes = True  # Ensure compatibility with SQLAlchemy models


class TipUpdate(BaseModel):
    content: Optional[str]
    problem_type: Optional[str]
    created_by: Optional[date]
