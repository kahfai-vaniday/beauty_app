# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.user.controllers import UserController
from app.user.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_user = Blueprint('user', __name__, url_prefix='/user')

# Set the route and accepted methods
@mod_user.route('/signin/', methods=['POST'])
def signin():

    result, status_code = UserController.controller_user_sign_in(request)

    return Response(json.dumps(result), status=status_code, mimetype='application/json')


@mod_user.route('/register/', methods=['POST'])
def register_user():

    result, status_code = UserController.controller_register_user(request)

    return Response(json.dumps(result), status=status_code, mimetype='application/json')
