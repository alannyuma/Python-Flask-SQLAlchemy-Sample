# .......................................................#
# Case model
# .......................................................#
from database import db
from tracker.users import models
from tracker.trials import models
from tracker.offences import models
# from sqlaclchemy.ext.declarative import declarative_base
# from sqlaclchemy.orm import relationship

# relationship table
case_subcribers=db.Table('case_subcribers', 
	db.Column('case_id',db.Integer,db.ForeignKey('cases.id'), nullable='false'),
	db.Column('user_id',db.Integer,db.ForeignKey('users.id'), nullable='false')
	# db.primarykeyConstraint('case_id','user_id')
	)

class Case(db.Model):

	__tablename__='cases'
	__searchable__ = ['name_of_accused', 'prosecutor']  # these fields will be indexed by whoosh


	id=db.Column(db.Integer, primary_key=True)
	arrest_date=db.Column(db.DateTime)
	name_of_accused=db.Column(db.String(255))
	status=db.Column(db.Boolean)
	offence_id=db.Column(db.Integer, db.ForeignKey('offences.id'))
	offence=db.relationship('Offences', backref='case', cascade='all')
	prosecutor=db.Column(db.String(255))
	sentence=db.Column(db.String(255))
	position_pior_case=db.Column(db.String(255))
	trial_id=db.Column(db.Integer, db.ForeignKey('trial.id'))
	trial=db.relationship('Trial', backref='case', cascade='all')
	user_case=db.relationship('User', secondary=case_subcribers, backref='case')
	# New instance instantiation procedure

	def __init__(self, arrest_date=None, name_of_accused=None, prosecutor=None):

		self.arrest_date  = arrest_date
		self.name_of_accused  = name_of_accused
		self.prosecutor = prosecutor

	def __unicode__(self):
		return self.name_of_accused

	# def __repr__(self):
	# 	return '<Case %r>' % (self.name_of_accused)




