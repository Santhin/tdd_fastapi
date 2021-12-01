# PRODUCTION, TESTING, ENVIRONMENT (dev)

import os
import logging

from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")



ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
TESTING = os.getenv("TESTING", 0)

class Settings(BaseSettings):
    environment: str = ENVIRONMENT
    testing: bool = TESTING


@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading settings')
    return Settings()