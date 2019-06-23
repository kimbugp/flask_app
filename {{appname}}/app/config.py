import os


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "{{app_name}}")
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = os.environ.get("DATABASE_DEV_URL")


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DATABASE_URI = os.environ.get("DATABASE_URL")