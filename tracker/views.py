from flask import render_template, Blueprint, request

blueprint_pages = Blueprint('pages', __name__)


########################################
############### home routes ############
########################################


@blueprint_pages.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@blueprint_pages.route('/about')
def about():
    return render_template('pages/placeholder.about.html')
