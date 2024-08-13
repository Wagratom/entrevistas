# app/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
