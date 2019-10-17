# Import the database object from the main app module

from flask import request, Response, json, make_response, jsonify
from flask.views import MethodView

from app import db

# Import module models (i.e. User)
from app.account.models import Account, Location
from app.user.models import User
from app.utils.alchemy_encoder import AlchemyEncoder
from app.utils.validation_functions import validate_jwt_token


class CreateNewAccountAPI(MethodView):

    @validate_jwt_token()
    def post(self):
        result = {"status": False, 'msg': 'Failed to create account!'}
        status_code = 400

        if 'business_name' in request.json.keys():

            user = request.user
            # create account
            business_name = request.json.get("business_name")
            accounts = Account.query.filter_by(business_name=business_name)

            if not accounts.count() and user:
                account = Account(business_name=business_name, creator_id=user.id)
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

        return Response(json.dumps(result), status=status_code, mimetype='application/json')


class GetAccountListAPI(MethodView):

    @validate_jwt_token()
    def post(self):
        result = {"status": False, 'data': []}
        status_code = 400

        # get logined user
        user = request.user
        if user:
            account_dict_list = []
            account_list = Account.query.filter_by(creator_id=user.id)

            for account in account_list:
                account_dict_list.append(json.loads(json.dumps(account, cls=AlchemyEncoder)))

            status_code = 200
            result['data'] = account_dict_list
        return Response(json.dumps(result), status=status_code, mimetype='application/json')


class GetAccountDetailsAPI(MethodView):

    @validate_jwt_token()
    def post(self):
        result = {"status": False, 'data': []}
        status_code = 400

        # get logined user
        user = request.user
        if user:
            account_id = request.json.get("account_id")

            account = Account.query.filter_by(id=account_id, creator_id=user.id).first()

            status_code = 200
            result['data'] = json.loads(json.dumps(account, cls=AlchemyEncoder))

        return Response(json.dumps(result), status=status_code, mimetype='application/json')
