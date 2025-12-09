import asyncio
import sys
from concurrent import futures

from grpc.aio import Server, server

from app.interceptors import interceptors
from app.registry import register


class GRPCHandler:

    def __init__(self, host: str = "::", port: int = 50051):
        self.host = host
        self.port = port

    def handle(self):
        async def _main() -> None:
            application: Server = server(
                futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
            )
            application.add_insecure_port(f"[{self.host}]:{self.port}")
            for service, servicer in register.items():
                servicer(service(), application)
            try:
                await application.start()
                sys.stdout.write(
                    f"Starting server at grpc://[{self.host}]:{self.port}\n"
                )
                await application.wait_for_termination()
            except asyncio.CancelledError:
                sys.stdout.write("\nStopping server...\n")
                await application.stop(5)

        try:
            asyncio.run(_main())
        except KeyboardInterrupt:
            sys.stdout.write("Server stop complete.\n")
