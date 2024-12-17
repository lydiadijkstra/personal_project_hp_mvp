from fastapi import APIRouter
from app.api.endpoints.tips.tips import tip_module

tip_router = APIRouter()


tip_router.include_router(
    tip_module,
    prefix="/tip",
    tags=["tip"],
    responses={404: {"description": "Not Found"}},
)
