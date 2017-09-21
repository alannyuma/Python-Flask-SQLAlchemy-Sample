# .......................................................#
# Case model
# .......................................................#
import constants as USER
#from tracker import db
from flask_sqlalchemy import SQLAlchemy
from database import db
#from tracker.cases import Case


class User(db.Model):

      __tablename__ = 'users'
      
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(50), unique=True)
      email = db.Column(db.String(120), unique=True)
      mobile = db.Column(db.String(50), unique=True)
      password = db.Column(db.String(120))
      role = db.Column(db.SmallInteger, default=USER.USER)
      status = db.Column(db.SmallInteger, default=USER.NEW)

      def __init__(self, name=None, email=None,mobile=None, password=None):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.password = password

      def getStatus(self):
        return USER.STATUS[self.status]

      def getRole(self):
        return USER.ROLE[self.role]

      def __unicode__(self):
        return self.name

      # def __repr__(self):
      #     return '<User %r>' % (self.name)