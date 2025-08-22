from app.repositories import HealthCheckRepository


class HealthCheckProcessor:
    def __init__(self):
        self.repository = HealthCheckRepository()

    async def check(self) -> str:
        """
        Check the health via DB.
        :return: str
        """
        return await self.repository.get_healthcheck_text()
