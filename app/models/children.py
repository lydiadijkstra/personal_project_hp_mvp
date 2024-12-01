from sqlalchemy import Column, String, Integer, ForeignKey, Date, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base


class Child(Base):
    __tablename__ = "children"

    child_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Child(child_id={self.child_id}, name={self.name}, difficulty={self.difficulty})>"
