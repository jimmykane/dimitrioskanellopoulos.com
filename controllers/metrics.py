
from models.users import RunkeeperUser
from lib.apis.runkeeperapi import RunkeeperAPI
import webapp2


class RunkeeperMetricsHandler(webapp2.RequestHandler):
    def get(self, user_id):
        runkeeper_user = RunkeeperUser.get_by_id(user_id)
        if not runkeeper_user:
            self.response.out.write('No user found')
        runkeeper_api = RunkeeperAPI(
            access_token=runkeeper_user.access_token,
            access_token_type=runkeeper_user.access_token_type,
            debug=True
        )
        pass
