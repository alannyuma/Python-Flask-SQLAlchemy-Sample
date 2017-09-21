# handles admin views
from flask.ext import admin
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.form import InlineFormAdmin
from flask.ext.admin.contrib.sqla.form import InlineModelConverter
from flask.ext.admin.contrib.sqla.fields import InlineModelFormList
from flask.ext.admin.model import BaseModelView

from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import filters

import flask.ext.whooshalchemy

from tracker.users import models as user_model
from tracker.cases import models as case_model
from tracker.trials import models as trial_model
from tracker.offences import models as offence_model

#admin.add_view(PostAdmin(Post,db.session))

# class Track(BaseView):
# 	@expose('/')
# 	def index(self):
# 		return self.render('index.html')

class CustomView(ModelView):

    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


class CaseAdmin(ModelView):

	can_view_details = True
	can_export = True
	column_searchable_list=('name_of_accused',)
	column_filters=('name_of_accused','prosecutor')
	#inline_models = [(Post, dict(form_columns=['title']))]
	# column_editable_list = ['title', 'body']
	# create_modal = True
	# edit_modal = True
	# form_excluded_columns = ('tags')
	inline_models = (user_model.User, )		


class TrialAdmin(ModelView):

	can_view_details = True
	can_export = True
	#inline_models = [(Post, dict(form_columns=['title']))]
	# column_editable_list = ['title', 'body']
	create_modal = True
	edit_modal = True
	# form_excluded_columns = ('tags')
	# inline_models = ['Post', ]	

class OffenceAdmin(ModelView):

	can_view_details = True
	can_export = True
	#inline_models = [(Post, dict(form_columns=['title']))]
	# column_editable_list = ['title', 'body']
	create_modal = True
	edit_modal = True
	# form_excluded_columns = ('tags')
	# inline_models = ['Post', ]	

class UserAdmin(ModelView):

	can_view_details = True
	can_export = True
	#inline_models = [(Post, dict(form_columns=['title']))]
	# column_editable_list = ['title', 'body']
	create_modal = True
	edit_modal = True

	inline_models = (case_model.Case, )		

	# form_excluded_columns = ('tags')
	# inline_models = ['Post', ]	


# class Post( Base ):
#     __tablename__ = 'posts'
#     id = Column( Integer, primary_key=True )
#     title = Column( Unicode( 255 ), nullable=False )
#     tags = relationship( 'Tag', backref='posts', secondary='taxonomy' )

# class Tag( Base ):
#     __tablename__ = 'tags'
#     id = Column( Integer, primary_key=True )
#     name = Column( Unicode( 255 ), nullable=False )

# taxonomy = Table(
#     'taxonomy', Base.metadata,
#     Column( 'post_id', Integer, ForeignKey( 'posts.id' ) ),
#     Column( 'tag_id', Integer, ForeignKey( 'tags.id' ) ),
# )

#  class PostModelView( ModelView ):
#         column_searchable_list = ( Post.title, Tag.name )
#         column_filters = (Post.title, Tag.name)

#         def init_search( self ):
#             r = super( PostModelView, self ).init_search()
#             #add the association table to search join list
#             self._search_joins.append(taxonomy)
#             #reverse the lsit so that the association table appears before the two main tables
#             self._search_joins.reverse()
#             return r

#         def scaffold_filters(self, name):
#             filters = super( PostModeView, self).scaffold_filters(name)
#             #Check if "tags" table has been processed and the join table added
#             if "tags" in self._filter_joins:
#               #add the association table to the filter join tables
#               self._filter_joins['tags'].append(taxonomy)
#               #reverse the list so that the association table appears before the two main tables
#               self._filter_joins['tags'].reverse()

#             return filters

