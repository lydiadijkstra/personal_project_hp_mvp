# fastapi
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


# import
from app.core.modules import init_routers, make_middleware
from app.core.database import initialize_database


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="HarmonicParent",
        description="Parenting API for supporting parents in times where bringing up gets hard. Developed with 💗 by Lydia.",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
        root_path=""

    )

    @app_.get("/", include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse(url="/docs")

    init_routers(app_=app_)

    return app_


#@app.get("/")async def root_redirect(): return RedirectResponse(url="/docs")

initialize_database()
app = create_app()


"""
install requirements, run command in terminal:
pip install -r requirements.txt

# or for updated version
pip install -r dev.txt

command to run the app:
uvicorn app.main:app --reload

to run the app locally go to app/core/database:
change the database settings from render to local

"""
