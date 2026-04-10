import os 
from sqlalchemy import create_engine  

class Config(object):
    SECRET_KEY ="claveSecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://montalvo:Jamr130705@127.0.0.1:3306/ico801_9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False