# advance global search 
# whoosh

from flask import Flask,render_template, Blueprint, request,url_for,session
from database import db
from .forms import SearchForm
# from views import blueprint_pages

blueprint_search = Blueprint('searcher', __name__)


@blueprint_search.route('/', methods=['GET', 'POST'])
def search():

    form = SearchForm(request.form)
    return render_template('searcher/search_result.html',query=SearchForm.search)



# from config import MAX_SEARCH_RESULTS

@blueprint_search.route('/search_results/<query>')
# @login_required
def search_results(query):
    results = db.Case.query.whoosh_search(query).all()
    return render_template('search_result.html',
                           query=query,
                           results=results)