import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

from app.settings import settings
from app.api.api_v1.api import api_router
from app.errors.app_errors import BaseError


app = FastAPI()

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

tags_metadata = [
    {
        "name": "Send question",
        "description": "Send question related to traveling or marketing",
    },
]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="AssistantsAI",
        version="1.0.0",
        description="AI assistant powered by gpt-3.5-turbo, answers "
        "questions related to traveling or marketing.",
        routes=app.routes,
        tags=tags_metadata,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(api_router)


@app.exception_handler(BaseError)
async def custom_exception_handler(_: Request, exc: BaseError):
    return JSONResponse(status_code=exc.code, content={"detail": exc.detail})
