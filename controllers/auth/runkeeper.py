import json

from controllers.server import register_required

import webapp2


from webapp2 import uri_for
from models.users import RunkeeperUserModel
from lib.apis.runkeeperapi import RunkeeperAPI
from google.appengine.api import users

from oauth2client.client import OAuth2WebServerFlow
from config.config import get_api_keys


class RunkeeperAuthHandler(webapp2.RequestHandler):
    def get_oauth2_flow(self):
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
    @register_required
    def get(self):
        self.redirect(str(self.get_oauth2_flow().step1_get_authorize_url()))


class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler):
    @register_required
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        runkeeper_credentials = self.get_oauth2_flow().step2_exchange(code=self.request.get('code'))
        access_token = runkeeper_credentials.token_response['access_token']
        access_token_type = runkeeper_credentials.token_response['token_type']

        runkeeper_api = RunkeeperAPI(
            access_token=access_token,
            access_token_type=access_token_type,
            debug=True
        )
        runkeeper_user = runkeeper_api.get_user()

        # Get or insert the model update tokens etc
        runkeeper_user_model = RunkeeperUserModel.get_or_insert(
            users.get_current_user().user_id(),
            credentials=runkeeper_credentials,
            runkeeper_user_id=str(runkeeper_user.user_id)
        )
        # Update
        runkeeper_user_model.populate(credentials=runkeeper_credentials, runkeeper_user_id=str(runkeeper_user.user_id))
        runkeeper_user_model.put()

        self.response.out.write('Success')