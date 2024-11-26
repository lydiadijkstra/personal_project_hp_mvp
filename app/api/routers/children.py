from fastapi import APIRouter
from app.api.endpoints.children.children import child_module
from app.api.endpoints.children.auth import auth_module

child_router = APIRouter()

child_router.include_router(
    child_module,
    prefix="/children",
    tags=["children"],
    responses={404: {"description": "Not found"}},
)

child_router.include_router(
    auth_module,
    prefix="",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

