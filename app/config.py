# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '9ycmsDAI435zDDDt2jxgsUDglSTdB1sDLMGVWkpiALE1x42lU0k3HM0h2OXST7FL'
    SQLALCHEMY_DATABASE_URI = 'postgresql://openpg:openpgpwd@localhost/sgrh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False