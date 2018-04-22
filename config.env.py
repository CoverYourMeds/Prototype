# Flask config
import os
from os import environ as env

# Flask config
DEBUG = True
IP = env.get('IP', 'localhost')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', 'localhost:8080')

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), "data.db"))
