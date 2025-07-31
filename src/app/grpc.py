import os

from app.core.grpc import get_grpc_application

os.environ.setdefault("SETTINGS_MODULE", "app.settings")

application = get_grpc_application()
