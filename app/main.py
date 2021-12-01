from fastapi import FastAPI, Depends

from .config import get_settings, Settings


app = FastAPI()





@app.get("/health", tags=['health'], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        }

