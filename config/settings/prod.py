from .base import *
from .base import env


SECRET_KEY = env("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db()
}