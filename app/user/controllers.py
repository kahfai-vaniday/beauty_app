# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.user.models import User


class UserController(object):

    @classmethod
    def controller_user_sign_in(cls, request):
        result = {"status": False, 'msg': 'Failed to login!', 'token': None}
        status_code = 400

        if request.method == 'POST' and 'email' in request.json.keys() and 'password' in request.json.keys():

            email = request.json.get("email")
            password = request.json.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password):

                    status_code = 200
                    result = {"status": True, 'msg': 'Successfully login.', 'token': user.token}
                else:
                    result['msg'] = "Wrong Password"
            else:
                result['msg'] = "User does not exist."
        return result, status_code

    @classmethod
    def controller_register_user(cls, request):
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
        return result, status_code