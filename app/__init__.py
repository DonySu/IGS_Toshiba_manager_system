from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views,models

if not app.debug:
    file_handler = RotatingFileHandler('log/microblog.log',maxBytes=1*1024*1024,backupCount=10)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [%(pathname)s:%(lineno)d]')
    file_handler.setFormatter(formatter)
    app.logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.info('Microblog startup:')
    app.logger.info("The server is under debuging.")
    app.logger.info("Any problem faced please contact DonySu~")
    app.logger.info("Thanks for your support.^_^")
