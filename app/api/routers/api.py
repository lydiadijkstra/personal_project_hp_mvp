from fastapi import APIRouter
from app.api.routers.user import user_router
from app.api.routers.children import child_router


router = APIRouter()

router.include_router(user_router)
router.include_router(child_router)

#
# import fastapi
#
#
# api = fastapi.FastAPI()
# #api.router.prefix = "/users"
# router = fastapi.APIRouter()
# #api.include_router(router, prefix="/")