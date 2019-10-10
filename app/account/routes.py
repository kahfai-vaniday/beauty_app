# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

# very important line for DB migration
from app.account import models

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_account = Blueprint('account', __name__, url_prefix='/account')

# Set the route and accepted methods
@mod_account.route('/create/', methods=['POST'])
def create_new_account():
    result = {}
    status_code = None
    return Response(json.dumps(result), status=status_code, mimetype='application/json')
