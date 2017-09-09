import os

basedir_local = os.path.dirname(__file__)
basedir = (os.path.abspath(basedir_local) + '/Database/')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')

CSRF_ENABLED = True
SECRET_KEY = 'donysu'

LIST_NUM_PER_PAGE = 10
