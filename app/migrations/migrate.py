from app.db import TORTOISE_CONFIG
from tortoise import Tortoise

async def migrate():
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    import asyncio
    asyncio.run(migrate())
