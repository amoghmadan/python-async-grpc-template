from app.repositories import HealthCheckRepository


class HealthCheckProcessor:
    def __init__(self):
        self.repo = HealthCheckRepository()

    async def check(self) -> str:
        return await self.repo.get_healthcheck_text()
