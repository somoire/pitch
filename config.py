import os
class Config:
    """
    General configuration parent class
    """
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
    Config: The parent confiuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://rodneysomoire:rodney99@localhost/pitch_test'

    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://rodneysomoire:rodney99@localhost/pitch'
    DEBUG = True


config_options={
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}