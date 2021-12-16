from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from .config import get_settings, Settings, DATABASE_STAGE_URL
from .models import BlogModel, BlogSchema, BlogSchemaCreate, PostModel, PostSchema, PostSchemaCreate
from tortoise import Tortoise
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter

app = FastAPI()

TORTOISE_ORM = {
    "connections": {"default": DATABASE_STAGE_URL},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        },
    },
}

# Create Database Tables
@app.on_event("startup")
async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

register_tortoise(app, config=TORTOISE_ORM)

router_blog = TortoiseCRUDRouter(
    schema=BlogSchema,
    create_schema=BlogSchemaCreate,
    db_model=BlogModel,
    prefix="blog"
)

router_post = TortoiseCRUDRouter(
    schema=PostSchema,
    create_schema=PostSchemaCreate,
    db_model=PostModel,
    prefix="post"
)

# Add it to your app
app.include_router(router_blog)
app.include_router(router_post)



@app.get("/health", tags=['health'], status_code=200)
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "database_stage_url": settings.database_stage_url,
        "database_dev_url" : settings.database_test_url
        }