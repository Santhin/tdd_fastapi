from fastapi import Depends, FastAPI

from .config import Settings, get_settings, log
from .db import init_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db(app)
    log.info("### Starting FastAPI ###")


@app.get("/health", tags=["health"], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "database_url": settings.database_url,
    }
