from flask import Flask,render_template,request,flash,redirect,url_for,session
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy


from wtforms import Form,TextField,validators
from wtforms.ext.sqlalchemy.orm import model_form


import flask.ext.whooshalchemy


class SearchForm(Form):
	 search = TextField(
        'name'
    )
