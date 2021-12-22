# PRODUCTION, TESTING, ENVIRONMENT (dev)

import os
import logging

from functools import lru_cache
from pydantic import BaseSettings, AnyUrl

import asyncpg


log = logging.getLogger("uvicorn")



DATABASE_STAGE_URL = os.getenv('DATABASE_STAGE_URL')
DATABASE_TEST_URL = os.getenv('DATABASE_TEST_URL')

ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
TESTING = os.getenv("TESTING", 0)

class Settings(BaseSettings):
    environment: str = ENVIRONMENT
    testing: bool = TESTING
    database_url: AnyUrl =  DATABASE_STAGE_URL


@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading settings')
    return Settings()




