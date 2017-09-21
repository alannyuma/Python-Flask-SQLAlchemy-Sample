import os
import sys
 
# handles admin views
from flask.ext import admin
from flask.ext.admin import Admin
from flask import Flask, render_template, url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
from users import views


# Elastic Search
from flask import Flask
from flask.ext.elasticsearch import FlaskElasticsearch

#from users import forms, models

from admin import views as admin_view
from database import db

#from flask.ext.superadmin import Admin, BaseView, expose, model
#from users.models import db

blueprint_users = Blueprint('user_pages', __name__)
blueprint_search = Blueprint('searcher', __name__)


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)



with app.test_request_context():

  import views as global_view


  # Define the blueprint: 'pages'
  app.register_blueprint(global_view.blueprint_pages)


  # users dependences
  from tracker.users import views
  from tracker.searcher import views as search_view


  from users import models as user_model
  # app models
  from cases import models as case_model
  from trials import models as trial_model
  from offences import models as offence_model

  # Introducing customize admin UX


  #   # Customized admin interface
  # class CustomView(ModelView):
  #     list_template = 'list.html'
  #     create_template = 'create.html'
  #     edit_template = 'edit.html'


  # class UserAdmin(CustomView):
  #     column_searchable_list = ('name',)
  #     column_filters = ('name', 'email')


  # # Flask views
  # @app.route('/')
  # def index():
  #     return '<a href="/admin/">Click me to get to Admin!</a>'


  # # Create admin with custom base template
  # admin = Admin(app, 'Example: Layout-BS3', base_template='admin/layout.html', template_mode='bootstrap3')

  # # Add views
  # admin.add_view(UserAdmin(User, db.session))
  # admin.add_view(CustomView(Page, db.session))


  # admin context and dependences

  admin = Admin(app, name='YukiYuki-Tracker Admin')
  # admin.add_view(admin_view.Track(name='Tracker'))
  # admin.add_view()
  admin.add_view(admin_view.CaseAdmin(case_model.Case,db.session))
  admin.add_view(admin_view.TrialAdmin(trial_model.Trial,db.session))
  admin.add_view(admin_view.OffenceAdmin(offence_model.Offences,db.session))
  admin.add_view(admin_view.UserAdmin(user_model.User,db.session))



  # Define the blueprint: 'Users'

  app.register_blueprint(views.blueprint_users)
  app.register_blueprint(search_view.blueprint_search)

  db.create_all()



 # register elastic searching

  es = FlaskElasticsearch(app)



########################
# Configure Secret Key #
########################
  app.config['SECRET_KEY'] = 'SECRET KEY'
  # def install_secret_key(app, filename='secret_key'):
  #     """Configure the SECRET_KEY from a file
  #     in the instance directory.

  #     If the file does not exist, print instructions
  #     to create it from a shell with a random key,
  #     then exit.
  #     """
  #     filename = os.path.join(app.instance_path, filename)

  #     try:
  #         app.config['SECRET_KEY'] = 'SECRET KEY'#open(filename, 'rb').read()
  #     except IOError:
  #         print('Error: No secret key. Create it with:')
  #         full_path = os.path.dirname(filename)
  #         if not os.path.isdir(full_path):
  #             print('mkdir -p {filename}'.format(filename=full_path))
  #         print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
  #         sys.exit(1)

  #     if not app.config['DEBUG']:
  #       install_secret_key(app)



@app.errorhandler(404)
def not_found_error(error):
  return render_template('errors/404.html'), 404


#from app.users.views import mod as usersModule
# #app.register_blueprint(usersModule)
# app.register_blueprint(error_page)


# Build the database:
# This will create the database file using SQLAlchemy



