"""
Default settings. Override these with settings in the module pointed to by the
SETTINGS_MODULE environment variable.
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""  # nosec: B105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition
GRPC_APPLICATION = ""

# Database settings
DATABASES: dict[str, dict[str, str]] = {}

# Internationalization
TIME_ZONE = "UTC"
USE_TZ = True
