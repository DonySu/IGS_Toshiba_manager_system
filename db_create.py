#!flask/bin/python3

from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path
import os

db.create_all()

os.system("flask/bin/python3 db_manage.py db init")

