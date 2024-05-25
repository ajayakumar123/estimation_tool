from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField ,SelectField
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
    task_details = StringField('Task Details', validators=[DataRequired(),Length(min=3, max=100)])
    task_complexity = SelectField('Complexity', choices=[('high','High'),('medium','Medium'),('low','Low')],
                                   validators=[DataRequired()])
    task_size = SelectField('Size', choices=[('large','Large'),('medium','Medium'),('small','Small')],
                            validators=[DataRequired()]) 
    task_type = SelectField('Type', choices=[('development','Development'),('testing','Testing'),
                                            ('deployment','Deployment'),('documentation','Documentation')], 
                            validators=[DataRequired()])

    additional_notes = TextAreaField('Additional Notes')
    estimated_effort = StringField('Estimated Effort',render_kw={'readonly': True})
    submit = SubmitField('Submit')