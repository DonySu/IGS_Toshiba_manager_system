#!flask/bin/python3

from app import app
from app import db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from config import basedir

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
