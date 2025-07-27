import importlib

from grpc.aio import Server

from app.services import HealthCheckService

healthcheck_pb2_grpc = importlib.import_module("healthcheck_pb2_grpc")


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
