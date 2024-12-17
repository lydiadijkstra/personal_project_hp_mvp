from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class Tip(BaseModel):
    tip_id: int
    user_id: int
    child_id: int
    content: str
    problem_type: Optional[str] = None
    send_at: datetime

    class Config:
        from_attributes = True  # Ensure compatibility with SQLAlchemy models
