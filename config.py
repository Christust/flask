class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TEST = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///api.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    DEBUG = False
    TEST = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    "development": DevelopmentConfig,
    "test": TestConfig
}