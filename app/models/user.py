from sqlalchemy import Column, String, Enum, TIMESTAMP, Integer, Boolean
from enum import Enum as PythonEnum
from app.core.database import Base
from .common import CommonModel
from sqlalchemy.sql import func


class UserRole(str, PythonEnum):
	user = "user"
	admin = "admin"

class User(CommonModel):
	__tablename__ = "users"

	user_id = Column(Integer, primary_key=True, index=True)
	user_name = Column(String, nullable=True)
	email = Column(String, unique=True, index=True, nullable=True)
	password = Column(String, nullable=False)
	name = Column(String)
	role = Column(Enum(UserRole), default=UserRole.user)
	location = Column(String)
	created_at = Column(TIMESTAMP, default=func.now(), nullable=False)


	def __repr__(self):
		return f"{self.email}"
	
metadata = Base.metadata
