import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")
    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgres://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

settings = Settings()
