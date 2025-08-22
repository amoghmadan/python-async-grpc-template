from grpc.aio import Server

from app.protobuf.healthcheck import healthcheck_pb2_grpc
from app.services import HealthCheckService


def register_services(server: Server) -> Server:
    """
    Register gRPC services with the application.
    :param server: Server, the grpc.aio.server instance.
    :return: Server
    """
    healthcheck_pb2_grpc.add_HealthCheckServiceServicer_to_server(
        HealthCheckService(), server
    )
    return server
