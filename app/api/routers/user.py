from fastapi import APIRouter
from app.api.endpoints.user.user import user_module
from app.api.endpoints.user.auth import auth_module, login_for_access_token

user_router = APIRouter()
child_router = APIRouter()


user_router.include_router(
    user_module,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found > app-api-routers-children.py - 1"}},
)

user_router.include_router(
    auth_module,
    prefix="/auth",
    tags=["auth"], # auth/login
    responses={404: {"description": "Not found > app-api-routers-children.py - 2"}},
)
