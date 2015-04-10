
from models.users import RunkeeperUserModel
from lib.apis.runkeeperapi import RunkeeperAPI
import webapp2


class RunkeeperMetricsHandler(webapp2.RequestHandler):
    def get(self, user_id):
        runkeeper_user_model = RunkeeperUserModel.get_by_id(user_id)
        if not runkeeper_user_model:
            self.response.out.write('No user found')
            return
        runkeeper_api = RunkeeperAPI(
            access_token=runkeeper_user_model.access_token,
            access_token_type=runkeeper_user_model.access_token_type,
            debug=True
        )
        runkeeper_user = runkeeper_api.get_user()
        runkeeper_user_profile = runkeeper_api.get_user_profile()
        a = runkeeper_user.profile
        pass
