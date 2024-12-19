from fastapi import APIRouter
from app.api.endpoints.tips.tips import tip_module

tip_router = APIRouter()


tip_router.include_router(
    tip_module,
    prefix="/tips",
    tags=["tips"],
    responses={404: {"description": "Not Found"}},
)
