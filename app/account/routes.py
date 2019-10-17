# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

# very important line for DB migration
from app import db
from app.account import models

# Define the blueprint: 'auth', set its url prefix: app.url/auth
from app.account.controllers import CreateNewAccountAPI, GetAccountListAPI, GetAccountDetailsAPI

mod_account = Blueprint('account', __name__, url_prefix='/account')


create_new_account_view = CreateNewAccountAPI.as_view('register_api')
get_account_list_view = GetAccountListAPI.as_view('get_account_list_api')
get_account_detail_view = GetAccountDetailsAPI.as_view('get_account_details_api')


mod_account.add_url_rule(
    '/create/',
    view_func=create_new_account_view,
    methods=['POST']
)

mod_account.add_url_rule(
    '/list/',
    view_func=get_account_list_view,
    methods=['POST']
)

mod_account.add_url_rule(
    '/details/',
    view_func=get_account_detail_view,
    methods=['POST']
)


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

    result, status_code = ShopController.controller_create_new_account_location(request)

    return Response(json.dumps(result), status=status_code, mimetype='application/json')


@mod_account.route('/location/list/', methods=['POST'])
def get_account_location_list():

    result, status_code = ShopController.controller_get_account_locations_list(request)

    return Response(json.dumps(result), status=status_code, mimetype='application/json')