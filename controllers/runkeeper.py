import json
import webapp2

from webapp2 import uri_for

from config.config import get_api_keys
from models.users import RunkeeperUser
from lib.apis.runkeeperapi import RunkeeperAPI
from lib.apis.authentication.runkeeper import RunkeeperAuth


class RunkeeperAuthHandler(object):
    @classmethod
    def get_runkeeper_auth(cls):
        return RunkeeperAuth(
            client_id=get_api_keys()['runkeeper']['client_id'],
            client_secret=get_api_keys()['runkeeper']['client_secret']
        )


class RunkeeperAuthCallHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        self.redirect(
            self.get_runkeeper_auth().get_authorize_url(self.request.host_url + uri_for('runkeeper_auth_callback')))


class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        runkeeper_auth_session = self.get_runkeeper_auth().get_auth_session(self.request.get('code'),
                                                                            self.request.host_url + uri_for(
                                                                                'runkeeper_auth_callback'))

        runkeeper_api = RunkeeperAPI(
            access_token=runkeeper_auth_session.access_token,
            access_token_type=json.loads(runkeeper_auth_session.access_token_response._content)['token_type'],
            debug=True
        )
        runkeeper_user = runkeeper_api.get_user()
        runkeeper_user_profile = runkeeper_api.get_user_profile()


        # Get or insert the model update tokens etc
        runkeeper_auth_model = RunkeeperUser.get_or_insert(
        )
        runkeeper_auth_model.populate(
        )
        runkeeper_auth_model.put()
        # Write the result
        self.response.out.write('Success')