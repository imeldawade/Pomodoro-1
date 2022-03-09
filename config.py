import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production class
    '''
    pass

class DevConfig(Config):
    DEBUG = True 

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}