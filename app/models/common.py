from sqlalchemy import Column, Boolean, Integer, String , DateTime, func
from app.core.database import Base


class CommonModel(Base):
    __abstract__ = True

    user_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
