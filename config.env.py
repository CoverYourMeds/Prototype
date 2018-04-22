# Flask config
import os
from os import environ as env

# Flask config
DEBUG = True
IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', '0.0.0.0:8080')

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), "data.db"))
