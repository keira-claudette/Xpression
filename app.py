from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
# intiat the app
app = Flask(__name__)
# creating a private key
app.config['SECRET_KEY'] = 'ea9bd0117494a936183776a12abdfd00'
# intialize the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Xpression/database.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    """
	    user class
		id = an integer that identify unique user
 		username= user name
		email= accept email unique for all user
		password = accept string
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    """ a method to query through db"""
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    """
	class  login form
	username = a string field cant be left blank validates input
	password =  validates input and it inforces input
	remember = a booleanfield that saves username and password
	"""
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    """
	RegisterForm class that registers new users
	email = accepts valid email address length of 50 if not gives error message
	username = accepts valid email addres with limited charachter length
	password =  validates password  if they are in acceptble range
	""" 
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    """ index route takes to home screen"""
    return render_template('index.html')

'''@app.route('/index')
@login_required
def index():
    return render_template('index.html', name=current_user.username)
'''

@app.route('/search', methods=['GET'] )
def search():
    """ search route recieves data from the html form susbmission and
        makes a GET request to GIPHY for search word input
    """
    url = 'https://api.giphy.com/v1/gifs/search?q="' + request.args['search'] + '"&api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&q=&limit=25&offset=0&rating=g&lang=en'
    resp = requests.get(url)
    '''resp.json()["data"][0]["images"]["fixed_height"]["url"]'''
    all = []
    for i in range(len(resp.json()["data"])):
        all.append(resp.json()["data"][i]["images"]["fixed_height"]["url"])
    return render_template('search.html', urls=all)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ a method to login the user to check that it querys the database for the values entered are similar"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + '' + form.password.data + '</h1>'
    return render_template('login.html', form=form)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ from registration form takes in the input  using hashed_password templates it changes the inputed password to 16 digit secret key"""
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
        #return '<h1>' + form.username.data + '' + form.email.data + '' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)

@app.route('/user')
@login_required
def user():
    """ a route to take to the user page"""
    return render_template('user.html')

@app.route('/logout')
@login_required
def logout():
    """ these route requires a login to work and as it sign out it takes to the home screen"""
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
