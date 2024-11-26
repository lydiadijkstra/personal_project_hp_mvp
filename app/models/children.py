from sqlalchemy import Column, String, Integer, ForeignKey, Date, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base
from .common import CommonModel


class Child(CommonModel):
    __tablename__ = "children"

    child_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)  # Fixed ForeignKey
    name = Column(String)
    difficulty = Column(String)
    birth_date = Column(Date)  # Import Date from sqlalchemy
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)

    def __repr__(self):
        name_display = self.name if self.name else "No Name"  # Default display if name is None
        return f"<Child(child_id={self.child_id}, name={name_display}, difficulty={self.difficulty})>"


metadata = Base.metadata
