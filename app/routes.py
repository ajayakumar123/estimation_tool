from flask import render_template,flash, redirect,url_for,request, jsonify 
from app import app,mongo, login_manager,bcrypt 
from flask_login import login_user, current_user, logout_user, login_required,UserMixin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from app.models import User
from app.forms import RegistrationForm,LoginForm,EstimationForm
from bson.objectid import ObjectId
from datetime import timedelta



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
        return redirect(url_for('estimation'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        password_check = bcrypt.check_password_hash(user.password, form.password.data)
        if user and password_check:
            login_user(user)
            return redirect(url_for('estimation'))
        else:
            flash('Login Faild. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/api/get_token', methods=['POST'])
def get_token():
    data = request.get_json()
    user = mongo.db.users.find_one({'email': data['email']})
    password_check = bcrypt.check_password_hash(user["password"], data["password"])
    if user and password_check:
        access_token = create_access_token(identity=data['email'], expires_delta=timedelta(hours=6))
        return jsonify(success=True, access_token=access_token)
    return jsonify(success=False), 401

@app.route('/api/get_estimate', methods=['POST'])
def get_estimate():
    data = request.get_json()
    complexity = data['task_complexity']
    size = data['task_size']
    task_type = data['task_type']
    query = {
        'complexity': complexity,
        'size': size,
        'type': task_type
    }
    count = mongo.db.historical_data.count_documents(query)
    if count == 0:
        estimate=False
        confidence_level=False
    else:
        estimated_efforts = []
        historical_data = mongo.db.historical_data.find(query)
        for task in historical_data:
            estimated_efforts.append(task.get('estimated_effort',0))
        estimate = sum(estimated_efforts)/len(estimated_efforts)
        estimate = round(estimate,2)
        confidence_level = "Low" if estimate<25 else "Medium" if estimate < 60 else "High"
    return jsonify(success=True, estimate=estimate, confidence_level=confidence_level)
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/estimation", methods=['GET', 'POST'])
@login_required
def estimation():
    form = EstimationForm()
    if form.validate_on_submit():
        data = { 
            "title":form.task_details.data,
            "complexity": form.task_complexity.data,
            "size": form.task_size.data,
            "type": form.task_type.data,
            "description": form.additional_notes.data,
            "estimated_effort":form.estimated_effort.data
            }
        mongo.db.historical_data.insert_one(data)
        flash('task added', 'success')
        return redirect(url_for('estimation'))
    return render_template('estimation.html', form=form)
