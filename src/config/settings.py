import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_int(name: str, default: int) -> int:
    return int(os.getenv(name, str(default)))


@dataclass(frozen=True)
class Settings:
    port: int
    env: str
    database_url: str

    @property
    def debug(self) -> bool:
        return self.env == "development"


def get_settings() -> Settings:
    return Settings(
        port=_get_int("PORT", 5000),
        env=os.getenv("ENV", "development"),
        database_url=os.getenv("DATABASE_URL", ""),
    )


settings = get_settings()
