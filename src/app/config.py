import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST")
ENVIRONMENT = os.getenv("ENVIRONMENT")
TESTING = os.getenv("TESTING")


class Settings(BaseSettings):
    environment: str = ENVIRONMENT
    testing: bool = TESTING
    database_url: AnyUrl = DATABASE_URL


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading settings")
    return Settings()
