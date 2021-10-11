from flask import Flask, app, json, jsonify, request, render_template, session
from flask.helpers import make_response
from flask_login import LoginManager, current_user, login_manager,login_required,login_user,logout_user,fresh_login_required
from Controller.user_mgmt import User
import os
from flask_cors import CORS
from View import intro
import datetime

os.environ['OAUTHLIB_INSECURE_TRANSPORT']='1'

app=Flask(__name__,static_url_path='/static')
CORS(app,supports_credentials=True)
app.secret_key='xnaud'

