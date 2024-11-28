# fastapi
from fastapi import FastAPI
from app.core.modules import init_routers, make_middleware
from app.api.routers.children import child_router


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="HarmonicParent",
        description="Parenting API for supporting parents in times where bringing up gets hard. Created with a fork of the FastAPI starter kit repo, developed with 💗 by mahmud.",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    app_.include_router(child_router)

    """
    @app_.get("/")
    def read_root():
        return {"message": "Welcome to the API"}
    """
    return app_


app = create_app()


"""
install requirements, run command in terminal:
pip install -r requirements.txt

# or for updated version
pip install -r dev.txt

command to run the app:
uvicorn app.main:app --reload

"""
