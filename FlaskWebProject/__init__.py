"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.INFO) 

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

fileHandler = logging.FileHandler('cmsapp.log')
fileHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)

app.logger.addHandler(handler)
app.logger.addHandler(fileHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
app.logger.info('CMS Application configured')

import FlaskWebProject.views
