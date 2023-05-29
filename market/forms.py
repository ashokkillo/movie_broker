from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a differnt username')
    
    def validate_email_address(self, email_to_check):
        email_address= User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a differnt email address')
    
    username = StringField(label='Username', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address :', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter password : ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password : ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
    
class LoginForm(FlaskForm):
    username = StringField(label='Username')
    password1 = PasswordField(label='Enter password : ')
    submit = SubmitField(label='Create Account')  