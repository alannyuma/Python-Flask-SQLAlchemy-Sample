from database import db
from tracker.users import models
from tracker.trials import models


##### offences #####

class Offences(db.Model):

	__tablename__='offences'
	__searchable__ = ['offence_name', 'description'] 

	id=db.Column(db.Integer,primary_key=True)
	offence_name=db.Column(db.String(255))
	description=db.Column(db.String(255))
	fines= db.Column(db.String(225))

	def __init__(self, offence_name=None, description=None, fines=None):

		self.offence_name   = offence_name 
		self.description = description
		self.fines = fines

	def __unicode__(self):
		return self.offence_name

	# def __repr__(self):
	# 	return '<Offence %r>' % (self.offence_name)