
from .config import DATABASE_STAGE_URL


TORTOISE_ORM = {
    "connections": {"default": DATABASE_STAGE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
