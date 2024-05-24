from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=3, max=17)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class EstimationForm(FlaskForm):
    task_details = TextAreaField('Task Details', validators=[DataRequired()])
    task_complexity = StringField('Complexity', validators=[DataRequired()])
    task_size = StringField('Size', validators=[DataRequired()])
    task_type = StringField('Type', validators=[DataRequired()])
    additional_notes = TextAreaField('Additional Notes')
    submit = SubmitField('Submit')