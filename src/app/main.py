from fastapi import Depends, FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .config import DATABASE_URL, Settings, get_settings

app = FastAPI()

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.get("/health", tags=["health"], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "database_url": settings.database_url,
    }
