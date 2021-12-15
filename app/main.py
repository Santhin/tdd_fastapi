from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from .config import get_settings, Settings, DATABASE_STAGE_URL

app = FastAPI()

register_tortoise(
    app,
    db_url=DATABASE_STAGE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/health", tags=['health'], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "database_stage_url": settings.database_stage_url,
        "database_dev_url" : settings.database_test_url
        }