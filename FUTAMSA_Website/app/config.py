import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('d60548a6324dab46a0f270686d5e9f5e')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://username:password@localhost/futamsa_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

