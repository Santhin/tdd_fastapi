from tortoise.contrib.fastapi import register_tortoise
from .config import DATABASE_STAGE_URL
from fastapi import FastAPI
from tortoise import Tortoise, run_async

def init_db(app: FastAPI):
    register_tortoise(
    app,
    db_url=DATABASE_STAGE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
    
    
async def generate_schemas():
    await Tortoise.init(db_url = DATABASE_STAGE_URL, modules = {"models": ["models"]})
    await Tortoise.generate_schemas()
    await Tortoise.close_connection()
    


if __name__ == "__main__":
    # TODO: add view models
    run_async(generate_schemas()) 