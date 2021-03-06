import os

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
     
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    print(MAIL_USERNAME)
    
class ProdConfig(Config):

    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thanos:qwerty@localhost/personalblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}
