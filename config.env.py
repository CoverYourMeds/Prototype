# Flask config
import os

DEBUG = True
IP = 'localhost'
PORT = '3000'
SERVER_NAME = 'localhost:3000'

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), "data.db"))
