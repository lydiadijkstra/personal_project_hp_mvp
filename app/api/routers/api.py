from fastapi import APIRouter
from app.api.routers.user import user_router
from app.api.routers.children import child_router
from app.api.routers.tips import tip_router


router = APIRouter()

router.include_router(user_router)
router.include_router(child_router)
router.include_router(tip_router)
