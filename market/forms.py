from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email_address = StringField(label='Email Address')
    password1 = PasswordField(label='Enter password : ')
    password2 = PasswordField(label='Confirm password : ')
    submit = SubmitField(label='Create Account')
    
    
class LoginForm(FlaskForm):
    username = StringField(label='Username')
    password1 = PasswordField(label='Enter password : ')
    submit = SubmitField(label='Create Account')