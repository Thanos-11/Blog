import os

class Config:

    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY =('blogrhymeswithjog')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thanos:qwerty@localhost/personalblog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    print(MAIL_USERNAME)
    
class ProdConfig(Config):
    pass
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
# class TestConfig(Config):
#     pass
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thanos:qwerty@localhost/personalblog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thanos:qwerty@localhost/personalblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
