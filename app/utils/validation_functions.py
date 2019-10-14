from functools import wraps

from app.user.models import User


def validate_token(request):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):

            if 'token' not in request.json.keys():
                return "Missing user token", 400

            token = request.json.get('token')
            users = User.query.filter_by(token=token)

            if users.count():
                ret = f(*args, **kwargs)
                return ret
            else:
                return "Invalid user token", 400

        return wrapped

    return decorator