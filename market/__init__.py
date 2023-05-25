from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
FORM_KEY = os.getenv('FORM_SECRET_KEY')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # Uniform resource Identifier(URI)
app.config['SECRET_KEY'] = FORM_KEY

######Database Intialize###########
db = SQLAlchemy()
db.init_app(app)

from market import routes
