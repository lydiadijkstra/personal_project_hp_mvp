from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base


class Tip(Base):
    __tablename__ = "tips"

    # Column definitions
    tip_id = Column(Integer, primary_key=True, index=True)  # Unique ID for each tip
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete="CASCADE"), nullable=False)  # ForeignKey to user
    child_id = Column(Integer, ForeignKey('children.child_id', ondelete="CASCADE"),
                      nullable=False)  # ForeignKey to child with cascade delete
    content = Column(String, nullable=False)  # Content of the tip
    problem_type = Column(String, nullable=True)  # Type of problem the tip is addressing (optional)
    send_at = Column(TIMESTAMP, default=func.now(), nullable=False)  # Timestamp when the tip was sent/generated

    def __repr__(self):
        return f"<Tip(tip_id={self.tip_id}, content={self.content}, problem_type={self.problem_type}, send_at={self.send_at})>"
