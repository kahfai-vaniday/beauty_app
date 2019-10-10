# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy

# Define the WSGI application object
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.routes import mod_user as user_module
from app.account.routes import mod_account as account_module

# Register blueprint(s)
app.register_blueprint(account_module)
app.register_blueprint(user_module)


migrate = Migrate(app, db)
# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()