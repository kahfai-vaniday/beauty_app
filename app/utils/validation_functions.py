from functools import wraps

from flask import make_response, jsonify, request

from app.user.controllers import AuthController
from app.user.models import User


def validate_jwt_token():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            # get the auth token
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
            else:
                auth_token = ''
            if auth_token:
                resp = AuthController.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    user = User.query.filter_by(id=resp).first()
                    if user:
                        request.user = user
                    else:
                        request.user = None
                    return f(*args, **kwargs)
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return make_response(jsonify(responseObject)), 401
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return make_response(jsonify(responseObject)), 401

        return wrapped

    return decorator