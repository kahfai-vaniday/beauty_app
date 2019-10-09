# import secrets
# from datetime import datetime
#
# from app.database import db
#
#
# class User(db.Model):
#     """The User object that owns tasks."""
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Unicode, nullable=False)
#     email = db.Column(db.Unicode, nullable=False)
#     password = db.Column(db.Unicode, nullable=False)
#     date_joined = db.Column(db.DateTime, nullable=False)
#     token = db.Column(db.Unicode, nullable=False)
#
#     def __init__(self, *args, **kwargs):
#         """On construction, set date of creation."""
#         super().__init__(*args, **kwargs)
#         self.date_joined = datetime.now()
#         self.token = secrets.token_urlsafe(64)

# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
import secrets
from app import db


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


# Define a User model
class User(Base):

    # User Name
    name = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    phone = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    token = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.token = secrets.token_urlsafe(64)

    def __repr__(self):
        return '<User %r>' % (self.name)