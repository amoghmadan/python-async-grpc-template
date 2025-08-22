from sqlalchemy import Result, TextClause, text

from app.db import session


class HealthCheckRepository:
    """
    Repository for database-level healthcheck operations.
    """

    query: TextClause = text("SELECT 'Pong' AS pong;")

    async def get_healthcheck_text(self) -> str:
        """
        Executes a simple DB query to confirm connectivity.
        :return: str
        """
        async with session() as db:
            result: Result = await db.execute(self.query)
            return result.scalar_one()
