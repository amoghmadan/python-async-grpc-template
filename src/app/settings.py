import sys
from pathlib import Path

# Add the generated wallet directory to the Python path
sys.path.append("gen/app/python")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).parent.parent
LOG_DIR = BASE_DIR.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")uki4xv@9e!b2^rax@qfcmp5#=^^*ziemm^tl1jv+f2nf9e#)$"  # nosec: B105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
GRPC_APPLICATION = "app.grpc.application"

# Database settings
DATABASES = {
    "default": {
        "url": "sqlite+aiosqlite:///db.sqlite3",
    }
}

# Internationalization
TIME_ZONE = "UTC"
USE_TZ = True


# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa: E501
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "debug.log",
            "formatter": "verbose",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 15,
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
