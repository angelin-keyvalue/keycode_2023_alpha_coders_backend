import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


config_settings = {
    'development': DevelopmentConfig
}