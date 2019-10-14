from app import db


# Define a base model for other database tables to inherit
class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    business_name = db.Column(db.String(255), nullable=False, unique=True)

    timezone = db.Column(db.String(128), nullable=True)
    time_format = db.Column(db.String(128), nullable=True)
    week_start = db.Column(db.String(128), nullable=True)
    appointment_color_source = db.Column(db.String(128), nullable=True)

    website = db.Column(db.String(255), nullable=True)
    facebook_page = db.Column(db.String(255), nullable=True)
    instagram_page = db.Column(db.String(255), nullable=True)

    location = db.relationship('Location', backref='location', lazy='dynamic')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '{}'.format(self.shop_name)


class Location(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    location_name = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    apt_suite_building = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(150), nullable=False)
    state = db.Column(db.String(150), nullable=False)
    zip_code = db.Column(db.String(100), nullable=False)

    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.location_name)