from fastapi import FastAPI, Depends
from .config import get_settings, Settings, log
from .db import init_db




app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db(app)
    log.info("Starting FastAPI")
    

@app.on_event("shutdown")
def shutdown_event():
    log.info("Shutting down FastAPI")


@app.get("/health", tags=['health'], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "database_stage_url": settings.database_stage_url,
        "database_dev_url" : settings.database_test_url
        }