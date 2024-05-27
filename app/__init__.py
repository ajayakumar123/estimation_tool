from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'estimation'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/estimation_db'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/estimation_db'
app.config['JWT_SECRET_KEY'] = 'estimation'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)

login_manager.login_view = '/'
login_manager.login_message_category = 'info'


from app import routes
from app import historical_data
res = historical_data.import_sample_data()