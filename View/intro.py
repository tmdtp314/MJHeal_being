from Controller.session_mgmt import Session
from datetime import datetime
from flask import Flask, Blueprint, request, render_template, redirect, url_for,session
from flask_login.utils import logout_user
from Controller.user_mgmt import User
from Controller.session_mgmt import User
from flask_login import login_user, current_user

intro_view = Blueprint('intro',__name__)

@intro_view.route('/signIn',methods=['GET','POST'])
def signIn():
    if request.method=='GET':
        return redirect(url_for('intro.signIn'))
    else:
        user=User.create(request.form['userID'],request.form['password'])