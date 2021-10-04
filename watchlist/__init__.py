import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='HARD TO GUESS'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:w@127.0.0.1:3306/watch'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db=SQLAlchemy(app)
login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user=User.query.get(int(user_id))
    return user
    
login_manager.login_view='login'
login_manager.login_message='Welcome'

@app.context_processor
def inject_user():
    from watchlist.models import User
    user=User.query.first()
    return dict(user=user)
    
from watchlist import views, errors, commands

