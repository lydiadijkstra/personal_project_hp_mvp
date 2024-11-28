from fastapi import APIRouter
from app.api.endpoints.children.children import child_module

child_router = APIRouter()


child_router.include_router(
    child_module,
    prefix="/children",
    tags=["children"],
    responses={404: {"description": "Not found"}},
)
