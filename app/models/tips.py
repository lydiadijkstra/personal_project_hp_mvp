from sqlalchemy import Column, String, Integer, ForeignKey, Date, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base


class Tip(Base):
    __tablename__ = "tips"

    tip_id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    problem_type = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Tips(tip_id={self.tip_id}, content={self.content}, problem_type={self.difficulty}, created_by={self.created_by})>"
