import json
import webapp2

from webapp2 import uri_for
from models.users import RunkeeperUserModel
from lib.apis.runkeeperapi import RunkeeperAPI
from oauth2client.client import OAuth2WebServerFlow
from config.config import get_api_keys


class RunkeeperAuthHandler(webapp2.RequestHandler):
    def get_oauth_flow(self):
        return OAuth2WebServerFlow(
            client_id=get_api_keys()['runkeeper']['client_id'],
            client_secret=get_api_keys()['runkeeper']['client_secret'],
            scope='',
            redirect_uri=self.request.host_url + uri_for('runkeeper_auth_callback'),
            user_agent=None,
            auth_uri=str(get_api_keys()['runkeeper']['urls']['authorization_url']),
            token_uri=str(get_api_keys()['runkeeper']['urls']['access_token_url']),
            revoke_uri=None
        )
    pass


class RunkeeperAuthCallHandler(RunkeeperAuthHandler):
    def get(self):
        self.redirect(str(self.get_oauth_flow().step1_get_authorize_url()))


class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler):
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        runkeeper_auth_session = self.get_oauth_flow().step2_exchange(code=self.request.get('code'))
        access_token = runkeeper_auth_session.access_token
        access_token_type = runkeeper_auth_session.token_response['token_type']

        runkeeper_api = RunkeeperAPI(
            access_token=access_token,
            access_token_type=access_token_type,
            debug=True
        )
        runkeeper_user = runkeeper_api.get_user()
        runkeeper_user_profile = runkeeper_user.profile()

        # Get or insert the model update tokens etc
        runkeeper_auth_model = RunkeeperUserModel.get_or_insert(
            str(runkeeper_user.user_id),
            access_token=access_token,
            access_token_type=access_token_type,
            name=runkeeper_user_profile['name'],
            profile=runkeeper_user_profile['profile'],
            large_picture=runkeeper_user_profile.get('large_picture')
        )

        # Update
        runkeeper_auth_model.populate(
            access_token=access_token,
            access_token_type=access_token_type,
            name=runkeeper_user_profile['name'],
            profile=runkeeper_user_profile['profile'],
            large_picture=runkeeper_user_profile.get('large_picture')
        )

        # Write blind again
        runkeeper_auth_model.put()

        # Write the result
        self.response.out.write('Success')