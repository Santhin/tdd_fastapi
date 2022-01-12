from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from .config import DATABASE_URL, log

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI):
    log.info("Init db")
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models"]},
        generate_schemas=True,  #
        add_exception_handlers=True,
    )


async def generate_schemas():
    log.info("Init tortoise")
    await Tortoise.init(db_url=DATABASE_URL, modules={"models": ["models"]})
    log.info("Generate schemas")
    await Tortoise.generate_schemas()
    await Tortoise.close_connection()


if __name__ == "__main__":
    # TODO: add view models
    run_async(generate_schemas())
