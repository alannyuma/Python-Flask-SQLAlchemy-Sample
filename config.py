import os

# from flaskext.mysql import MySQL
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from flask_sqlalchemy import SQLAlchemy
_basedir = os.path.abspath(os.path.dirname(__file__))

# DEBUG = False

# mysql = MySQL()
# app = Flask(__name__)
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
# app.config['MYSQL_DATABASE_DB'] = 'yukiyukitracker_db'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:12345@localhost/yukiyukitracker_db'
# mysql.init_app(app)
SQLALCHEMY_DATABASE_URI='mysql://root:12345@localhost/yukiyukitracker_db'
WHOOSH_BASE = os.path.join(_basedir,'SQLALCHEMY_DATABASE_URI')


ELASTICSEARCH_HOST = "localhost:5000/es"
# #migration
# migrate = Migrate(app,db)
# manager=Manager(app)
# manager.add_command('db',MigrateCommand)

# #migrations
# manager.run()

# ADMINS = frozenset(['youremail@yourdomain.com'])
# SECRET_KEY = 'This string will be replaced with a proper key in production.'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
# DATABASE_CONNECT_OPTIONS = {}

# THREADS_PER_PAGE = 8

# WTF_CSRF_ENABLED = True
# WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

# RECAPTCHA_USE_SSL = False
# RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
# RECAPTCHA_OPTIONS = {'theme': 'white'}