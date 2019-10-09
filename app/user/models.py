# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
import secrets
# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash
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
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)

    phone = db.Column(db.String(128), nullable=True)
    address = db.Column(db.String(128), nullable=True)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=True)
    status = db.Column(db.SmallInteger, nullable=True)

    token = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.token = secrets.token_urlsafe(64)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    @classmethod
    def set_password_class_method(cls, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)