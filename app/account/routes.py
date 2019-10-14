# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

# very important line for DB migration
from app import db
from app.account import models

# Define the blueprint: 'auth', set its url prefix: app.url/auth
from app.account.controllers import ShopController
from app.utils.validation_functions import validate_token

mod_account = Blueprint('account', __name__, url_prefix='/account')


@mod_account.route('/create/', methods=['POST'])
@validate_token(request)
def create_new_account():

    result, status_code = ShopController.controller_create_new_account(request)

    return Response(json.dumps(result), status=status_code, mimetype='application/json')


@mod_account.route('/list/', methods=['POST'])
def get_account_list():
    result = {}
    status_code = None
    return Response(json.dumps(result), status=status_code, mimetype='application/json')


@mod_account.route('/update/', methods=['POST'])
def update_existing_account():
    result = {}
    status_code = None
    return Response(json.dumps(result), status=status_code, mimetype='application/json')


@mod_account.route('/delete/', methods=['POST'])
def delete_existing_account():
    result = {}
    status_code = None
    return Response(json.dumps(result), status=status_code, mimetype='application/json')


# LOCATION
@mod_account.route('/create_new_location/', methods=['POST'])
def create_new_location_for_account():
    result = {}
    status_code = None

    return Response(json.dumps(result), status=status_code, mimetype='application/json')