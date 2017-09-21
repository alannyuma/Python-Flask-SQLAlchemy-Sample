from flask_sqlalchemy import SQLAlchemy
# from SQLAlchemy import Integer, ForeignKey,String, Column
# from sqlaclchemy.ext.declarative import declarative_base
# from sqlaclchemy.orm import relationship
from database import db
from tracker.cases import *

class Trial(db.Model):
	__tablename__='trial'
	id=db.Column(db.Integer, primary_key=True)
	trial_date=db.Column(db.DateTime)
	status=db.Column(db.String(255))
	name_of_accused=db.Column(db.String(255))
	outcome=db.Column(db.String(255))


	# New instance instantiation procedure
	def __init__(self, trial_date=None, name_of_accused=None, outcome=None):

		self.trial_date  = trial_date
		self.name_of_accused  = name_of_accused
		self.outcome = outcome

	def __unicode__(self):
		return self.name_of_accused

	# def __repr__(self):
	# 	return '<Trial %r>' % (self.name_of_accused)


        