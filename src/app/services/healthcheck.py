# mypy: ignore-errors
import importlib

from sqlalchemy import Result, TextClause, text

from app.db import session

healthcheck_pb2 = importlib.import_module("healthcheck_pb2")
healthcheck_pb2_grpc = importlib.import_module("healthcheck_pb2_grpc")


class HealthCheckService(healthcheck_pb2_grpc.HealthCheckServiceServicer):
    """Servicer: Health Check Service"""

    async def Ping(self, request, context) -> healthcheck_pb2.PingResponse:
        """Ping SQL"""
        statement: TextClause = text("SELECT 'Pong' AS pong;")
        async with session() as db:
            result: Result = await db.execute(statement)
            string: str = result.scalar_one()
        return healthcheck_pb2.PingResponse(reply=string)
