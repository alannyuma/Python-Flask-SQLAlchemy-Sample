from tracker import app
from database import db
# handles migrations
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_DATABASE_URI, WHOOSH_BASE

#init logging
# from logging.config import fileConfig
# import logging

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#fileConfig(config.config_file_name)
#logger = logging.getLogger('alembic.env')

if __name__ == "__main__":
	#db.create_all()
	manager.run()
	#logger.info('Alan No changes in schema detected.')
	app.run(debug=True)




# update


# admin = User.query.filter_by(username='admin').first()
# admin.email = 'my_new_email@example.com'
# db.session.commit()

# user = User.query.get(5)
# user.name = 'New Name'
# db.session.commit()

# @app.route('/user/<username>')
# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)



# many to many insert

# You don't need to add anything directly to your association table, SQLAlchemy will do that. This is more or less from SQLAlchemy documentations:

# association_table = db.Table('association', db.Model.metadata,
#     db.Column('left_id', db.Integer, db.ForeignKey('left.id')),
#     db.Column('right_id', db.Integer, db.ForeignKey('right.id'))
# )

# class Parent(db.Model):
#     __tablename__ = 'left'
#     id = db.Column(db.Integer, primary_key=True)
#     children = db.relationship("Child",
#                     secondary=association_table)

# class Child(db.Model):
#     __tablename__ = 'right'
#     id = db.Column(db.Integer, primary_key=True)


# p = Parent()
# c = Child()
# p.children.append(c)
# db.session.add(p)
# db.session.commit()

# student_identifier = db.Table('student_identifier',
#     db.Column('class_id', db.Integer, db.ForeignKey('classes.class_id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('students.user_id'))
# )

# class Student(db.Model):
#     __tablename__ = 'students'
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_fistName = db.Column(db.String(64))
#     user_lastName = db.Column(db.String(64))
#     user_email = db.Column(db.String(128), unique=True)


# class Class(db.Model):
#     __tablename__ = 'classes'
#     class_id = db.Column(db.Integer, primary_key=True)
#     class_name = db.Column(db.String(128), unique=True)
#     children = db.relationship("Student",
#                     secondary=student_identifier)

# s = Student()
# c = Class()
# c.children.append(s)
# db.session.add(c)
# db.session.commit()

# one to many insert
 # import datetime
 # u = models.User.query.get(1)
 # p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
 # db.session.add(p)
 # db.session.commit()

 # search_term is a string that will get converted to a `tsvector` type by sqlalchemy

# def search(search_term):
#     return db.session.query(
#         db.distinct(SearchView.contract_id)
#     ).filter(db.or_(
#         SearchView.tsv_company_name.match(search_term, postgresql_regconfig='english'),
#         SearchView.tsv_line_item_description.match(search_term, postgresql_regconfig='english'),
#         SearchView.tsv_contract_description.match(search_term, postgresql_regconfig='english'),
#         SearchView.tsv_detail_value.match(search_term, postgresql_regconfig='english')
#     )).all()