from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class TipBase(BaseModel):
    problem_type: Optional[str] = None


class TipCreate(TipBase):
    pass


class Tip(TipBase):
    tip_id: int
    user_id: int
    child_id: int
    content: str
    send_at: datetime

    class Config:
        from_attributes = True
