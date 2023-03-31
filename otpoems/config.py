import os

class Config(object):
    SECRET_KEY = 'dev'
    #SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = "postgresql://bryanwgranger@localhost/otpoems"
