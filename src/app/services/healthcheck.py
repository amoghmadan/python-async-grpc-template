from app.processors import HealthCheckProcessor
from app.protobuf.healthcheck import healthcheck_pb2, healthcheck_pb2_grpc


class HealthCheckService(healthcheck_pb2_grpc.HealthCheckServiceServicer):
    """Servicer: Health Check Service"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processor = HealthCheckProcessor()

    async def Ping(self, request, context):
        """Ping SQL"""
        reply: str = await self.processor.check()
        return healthcheck_pb2.PingResponse(reply=reply)
