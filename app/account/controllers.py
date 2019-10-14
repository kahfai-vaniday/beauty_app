# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.account.models import Account, Location
from app.user.models import User


class ShopController(object):

    @classmethod
    def controller_create_new_account(cls, request):
        result = {"status": False, 'msg': 'Failed to create account!'}
        status_code = 400

        if request.method == 'POST' and 'business_name' in request.json.keys() and 'token' in request.json.keys():

            # get logined user
            user = User.query.filter_by(token=request.json.get("token")).first()

            # create account
            business_name = request.json.get("business_name")
            account = Account(business_name=business_name,
                              creator_id=user.id)
            db.session.add(account)
            db.session.commit()

            # create location
            location_name = request.json.get('location_name')
            contact_number = request.json.get('contact_number')
            contact_email = request.json.get('contact_email')
            street_address = request.json.get('street_address')
            apt_suite_building = request.json.get('apt_suite_building')
            city = request.json.get('city')
            state = request.json.get('state')
            zip_code = request.json.get('zip_code')

            # create location
            location = Location(location_name=location_name,
                                contact_number=contact_number,
                                contact_email=contact_email,
                                street_address=street_address,
                                apt_suite_building=apt_suite_building,
                                city=city,
                                state=state,
                                zip_code=zip_code,
                                account_id=account.id,
                                creator_id=user.id)
            db.session.add(location)
            db.session.commit()

            status_code = 200
            result = {"status": True, 'msg': 'Successfully create account.'}

        return result, status_code
