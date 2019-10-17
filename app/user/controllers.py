# Import the database object from the main app module
import datetime

import jwt
from flask.views import MethodView
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

from app import db, app

# Import module models (i.e. User)
from app.user.models import User
from config import SECRET_KEY


class AuthController(object):

    @classmethod
    def encode_auth_token(cls, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @classmethod
    def decode_auth_token(cls, auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class RegisterAPI(MethodView):

    def post(self):
        result = {"status": False, 'msg': ''}
        status_code = 400
        if request.method == 'POST':

            email = request.json.get("email")
            first_name = request.json.get("first_name")
            last_name = request.json.get("last_name")
            password = request.json.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                result['msg'] = "User already exist!"
            else:
                user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            password=User.set_password_class_method(password))
                db.session.add(user)
                db.session.commit()
                status_code = 201
                result = {"status": True, 'msg': 'User created successfully.'}
        return Response(json.dumps(result), status=status_code, mimetype='application/json')


class UserSignInAPI(MethodView):

    def post(self):
        result = {"status": False, 'msg': 'Failed to login!', 'token': None}
        status_code = 400

        if request.method == 'POST' and 'email' in request.json.keys() and 'password' in request.json.keys():

            email = request.json.get("email")
            password = request.json.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password):

                    auth_token = str(AuthController.encode_auth_token(user.id), 'utf-8')
                    status_code = 200
                    result = {"status": True, 'msg': 'Successfully login.', 'token': auth_token}
                else:
                    result['msg'] = "Wrong Password"
            else:
                result['msg'] = "User does not exist."
        return Response(json.dumps(result), status=status_code, mimetype='application/json')
