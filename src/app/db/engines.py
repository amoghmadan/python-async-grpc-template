from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.conf import settings

engines: dict[str, AsyncEngine] = {
    alias: create_async_engine(**kwargs)
    for alias, kwargs in settings.DATABASES.items()  # type: ignore[attr-defined]
}
