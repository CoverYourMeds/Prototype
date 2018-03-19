# Flask config
import os

DEBUG = True
IP = '0.0.0.0'
PORT = '8080'
SERVER_NAME = '0.0.0.0:8080'

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), "data.db"))
