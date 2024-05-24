from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'estimation'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/estimation_db'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = '/'
login_manager.login_message_category = 'info'

from app import routes