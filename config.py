import os
from re import DEBUG
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kev2214@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'kevoneverything'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kevohronoh@gmail.com'
    MAIL_PASSWORD = 'alicerono2214'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    ''' 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kev2214@localhost/blog'

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kev2214@localhost/blog'
    
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}