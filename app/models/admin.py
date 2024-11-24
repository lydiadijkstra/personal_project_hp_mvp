from sqladmin import ModelView
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.user_id,           # Corrected to match the db column name
        User.user_name,         # Corrected to match the db column name
        User.password,          # Corrected to match the db column name
        User.email,             # Corrected to match the db column name
        User.location,          # Corrected to match the db column name
        User.created_at,        # Corrected to match the db column name
        User.role,              # Corrected to match the db column name
    ]
