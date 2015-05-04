import json


from config.config import is_dev_server
from lib.apis.google_plus_api import GooglePlusAPI
from models.users import GooglePlusUserModel

import webapp2


class GooglePlusAPIHandler(webapp2.RequestHandler):
    disallowed_calls = [

    ]

    def get(self, user_id, call):
        # If its not allowed gto
        if not is_dev_server() and call in self.disallowed_calls:
            self.response.out.write('Call not allowed')
            return
        google_plus_user_model = GooglePlusUserModel.get_by_id(user_id)
        if not google_plus_user_model:
            self.response.out.write('No user found')
            return
        google_plus_api = GooglePlusAPI(credentials=google_plus_user_model.credentials)
        google_plus_user = GooglePlusAPI.get_user()
        pass


