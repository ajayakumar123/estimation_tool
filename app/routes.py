from flask import render_template,flash, redirect,url_for 
from app import app,mongo, login_manager,bcrypt 
from flask_login import login_user, current_user, logout_user, login_required,UserMixin
from app.models import User
from app.forms import RegistrationForm,LoginForm,EstimationForm
from bson.objectid import ObjectId
import pdb



@login_manager.user_loader
def load_user(user_id):
    '''function to load user after login'''
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_id, user_data['user_name'], user_data['email'], user_data['password'])
    return None

@app.route("/")
@app.route("/home")
def home():
    '''Hompage redirect router'''
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''helpful for user registration
        i/p: user_name,email,password and confirm password
    '''

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.create_user(form.user_name.data, form.email.data, form.password.data)
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''helpful for authenticate user based on email and password'''

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        password_check = bcrypt.check_password_hash(user.password, form.password.data)
        if user and password_check:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Faild. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/estimation", methods=['GET', 'POST'])
@login_required
def estimation():
    form = EstimationForm()
    print("111111111",form)
    if form.validate_on_submit():
        # estimation = get_estimation(form.task_details.data, form.task_complexity.data, form.task_size.data, form.task_type.data)
        estimation = 2.456
        flash(f'Estimated Effort: {estimation}', 'success')
        return redirect(url_for('estimate'))
    print("2222222222222",form)
    return render_template('estimation.html', form=form)
