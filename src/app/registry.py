from app.protobuf.healthcheck import healthcheck_pb2_grpc
from app.services import HealthCheckService

register = {
    HealthCheckService: healthcheck_pb2_grpc.add_HealthCheckServiceServicer_to_server,
}
