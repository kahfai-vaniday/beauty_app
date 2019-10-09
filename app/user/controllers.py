# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, Response, json

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.user.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_user = Blueprint('user', __name__, url_prefix='/user')

# Set the route and accepted methods
@mod_user.route('/signin/', methods=['GET', 'POST'])
def signin():

    print("Test")
    # # If sign in form is submitted
    # form = LoginForm(request.form)
    #
    # # Verify the sign in form
    # if form.validate_on_submit():
    #
    #     user = User.query.filter_by(email=form.email.data).first()
    #
    #     if user and check_password_hash(user.password, form.password.data):
    #
    #         session['user_id'] = user.id
    #
    #         flash('Welcome %s' % user.name)
    #
    #         return redirect(url_for('auth.home'))
    #
    #     flash('Wrong email or password', 'error-message')

    return Response(json.dumps({"haha":"1212", "gogo": 3343}), status=200, mimetype='application/json')