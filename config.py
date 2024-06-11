import os

basedir = os.path.abspath(os.path.dirname(__file__)) 
class Config:
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(basedir, "app.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = True
    TESTING = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
