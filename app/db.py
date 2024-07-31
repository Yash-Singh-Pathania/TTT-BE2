from tortoise import Tortoise
from app.settings import settings

TORTOISE_CONFIG = {
    'connections': {
        'default': settings.DATABASE_URL,
    },
    'apps': {
        'models': {
            'models': ['app.models'],
            'default_connection': 'default',
        },
    },
}

async def init():
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()
