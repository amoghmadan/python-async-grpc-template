from grpc.aio import ServerInterceptor

from app.interceptors.logging import AsyncLoggingInterceptor

interceptors: list[ServerInterceptor] = [AsyncLoggingInterceptor()]

__all__ = ["interceptors"]
