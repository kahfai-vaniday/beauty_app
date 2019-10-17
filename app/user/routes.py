# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

from app.user.controllers import RegisterAPI, UserSignInAPI
from app.user import models

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_user = Blueprint('user', __name__, url_prefix='/user')


# define the API resources
registration_view = RegisterAPI.as_view('register_api')
user_signin_view = UserSignInAPI.as_view('user_signin_api')

# add Rules for API Endpoints
mod_user.add_url_rule(
    '/register/',
    view_func=registration_view,
    methods=['POST']
)

mod_user.add_url_rule(
    '/signin/',
    view_func=user_signin_view,
    methods=['POST']
)