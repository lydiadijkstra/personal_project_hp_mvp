from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.user import UserRole


class UserBase(BaseModel):
	email: str


class UserCreate(UserBase):
	password: str
	name: Optional[str]
	role: Optional[str] = 'user'  # Default role is 'user'
	user_name: Optional[str]
	location: Optional[str]


class UserLogin(UserBase):
	password: str


class User(UserBase):
	user_id: int
	user_name: Optional[str]
	password: Optional[str] # only for debugging etc, turn off when app gets deployed
	name: Optional[str]
	location: Optional[str]
	role: UserRole or None
	created_at: datetime

	class Config:
		from_attributes = True


class UserUpdate(BaseModel):
	user_name: Optional[str]
	password: Optional[str]
	name: Optional[str]
	location: Optional[str]
	role: UserRole or None = None


class Token(BaseModel):
	access_token: str
	refresh_token: str
	token_type: str
