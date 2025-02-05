# fastapi 
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# sqlalchemy
from sqladmin import Admin, ModelView

# import 
from app.core.database import engine
from app.models.admin import UserAdmin
from app.api.routers.api import router

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)
    admin = Admin(app_, engine)
    admin.add_view(UserAdmin)


origins = [
    "*"
]

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    return middleware
