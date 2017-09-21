from flask import Flask,render_template, Blueprint, request,url_for,session
from .forms import LoginForm,RegisterForm, ForgotForm
from .models import User
from database import db

from werkzeug import check_password_hash, generate_password_hash
# from views import blueprint_pages

blueprint_users = Blueprint('user_pages', __name__)

# handles form events login, register, forget
@blueprint_users.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error=None
    if request.method =='POST':
    	if request.form['name']!='name':
    		error='Invalid username'
    	elif request.form['password']!='password':
    		error='Invalid password'
    	else:
    		session['logged_in']=True
    		flash('You were logged in')
    		return redirect(url_for('pages.home'), error=error)
    return render_template('users/login.html', form=form)


@blueprint_users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    error=None
    if request.method=='POST':
        register=User(form.name.data, form.email.data, form.password.data, form.confirm.data)
        db.session.add(register)
        db.session.commit()


    return render_template('users/register.html', form=form)


@blueprint_users.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotForm(request.form)
    return render_template('users/forgot.html', form=form)




# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# # error = None
# # if request.method == 'POST':
# # if request.form['username'] != app.config['USERNAME']:
# # error = 'Invalid username'
# # elif request.form['password'] != app.config['PASSWORD']:
# # error = 'Invalid password'
# # else:
# # session['logged_in'] = True
# # flash('You were logged in')
# # return redirect(url_for('show_entries'))
# # return render_template('login.html', error=error




# # @app.route('/logout')
# # def logout():
# # session.pop('logged_in', None)
# # flash('You were logged out')
# # return redirect(url_for('show_entries'))