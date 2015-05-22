import json


from config.config import is_dev_server
from lib.apis.google_plus_api import GooglePlusAPI
from models.users import GooglePlusUserModel
from controllers.server import MemcachedHandler, JSONReplyHandler


class GooglePlusAPIHandler(MemcachedHandler, JSONReplyHandler):
    allowed_calls = [
        'get_profile',
        'get_activities'
    ]

    def get(self, user_id, call):
        # If its not allowed gto
        if not is_dev_server() and call not in self.allowed_calls:
            self.response.out.write('Call not allowed')
            return
        google_plus_user_model = GooglePlusUserModel.query().filter(GooglePlusUserModel.google_plus_user_id == user_id).get()
        if not google_plus_user_model:
            self.response.out.write('No user found')
            return
        google_plus_api = GooglePlusAPI(credentials=google_plus_user_model.credentials)
        google_plus_user = google_plus_api.get_user()

        # Check if the call is an attribute
        if call not in dir(google_plus_user):
            self.response.out.write('Unknown call')
            return

        # Check if we can get from the cache
        response = self.get_from_memcache(user_id, call)
        if not response:
            # If not found call and write to cache
            response = getattr(google_plus_user, call)()
            self.add_to_memcache(self.get_cache_key(user_id, call), response)

        # Run the call and echo it
        self.json_dumps_response(response)