from sqladmin import ModelView
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.user_id,
        User.user_name,
        User.password,
        User.email,
        User.location,
        User.created_at,
        User.role,
    ]
