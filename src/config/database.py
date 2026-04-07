from ssl import create_default_context
from urllib.parse import parse_qs, unquote, urlparse

import pg8000

from src.config.settings import settings


def get_connection():
    if not settings.database_url:
        raise ValueError("DATABASE_URL is not configured")

    parsed = urlparse(settings.database_url)
    if parsed.scheme not in ("postgres", "postgresql"):
        raise ValueError("DATABASE_URL must start with postgres:// or postgresql://")

    query = parse_qs(parsed.query)
    sslmode = (query.get("sslmode", [""])[0] or "").lower()

    connect_kwargs = {
        "user": unquote(parsed.username or ""),
        "password": unquote(parsed.password or ""),
        "host": parsed.hostname or "localhost",
        "port": parsed.port or 5432,
        "database": parsed.path.lstrip("/"),
    }

    if sslmode in ("require", "verify-ca", "verify-full"):
        connect_kwargs["ssl_context"] = create_default_context()

    return pg8000.dbapi.connect(**connect_kwargs)
