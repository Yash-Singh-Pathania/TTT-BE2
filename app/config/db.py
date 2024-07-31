# app/config/db.py

from tortoise import Tortoise
from app.settings import settings

DATABASE_CONFIG = {
    "connections": {
        "default": settings.DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": ["app.models"],
            "default": True,
        }
    }
}

async def init_db():
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
