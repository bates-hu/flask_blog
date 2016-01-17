#coding:utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pagedown import PageDown
import os
from flask.ext.login import LoginManager
from config import basedir
from momentjs import momentjs


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
pagedown = PageDown()
pagedown.init_app(app)
lm.init_app(app)
lm.login_view = 'login'
app.jinja_env.globals['momentjs'] = momentjs

from app import views, models


