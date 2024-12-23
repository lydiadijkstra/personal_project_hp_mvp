# fastapi
from fastapi import FastAPI

# import
from app.core.modules import init_routers, make_middleware
from app.core.database import initialize_database


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="HarmonicParent",
        description="Parenting API for supporting parents in times where bringing up gets hard. Created with a fork of the FastAPI starter kit repo, developed with 💗 by mahmud.",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
        #root_path="/"

    )
    init_routers(app_=app_)

    return app_

initialize_database()
app = create_app()


"""
install requirements, run command in terminal:
pip install -r requirements.txt

# or for updated version
pip install -r dev.txt

command to run the app:
uvicorn app.main:app --reload

"""
