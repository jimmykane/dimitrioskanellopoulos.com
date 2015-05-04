import logging
import webapp2

from controllers.server import register_required
from models.users import GooglePlusUserModel, UserModel

from webapp2 import uri_for
from config.config import get_client_secrets_filename
from apiclient.discovery import build

from google.appengine.api import users

from oauth2client.client import flow_from_clientsecrets




class GoogleAuthHandler(webapp2.RequestHandler):
    def get_oauth2_flow(self, scope=None):
        return flow_from_clientsecrets(
            get_client_secrets_filename(),
            # Should use the above var but now is off due to sec concerns
            # @todo build dynamic routes to callbacks
            scope='https://www.googleapis.com/auth/plus.login',
            redirect_uri=self.request.host_url + uri_for('google_auth_callback')
        )
    pass


class GoogleAuthCallHandler(GoogleAuthHandler):

    @register_required
    def get(self, scope):
        self.redirect(str(self.get_oauth2_flow().step1_get_authorize_url()))
        pass


class GoogleAuthCallbackHandler(GoogleAuthHandler):
    @register_required
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get Credentials
        google_credentials = self.get_oauth2_flow().step2_exchange(self.request.params.get('code'))
        # @todo remove google plus stub
        # Build the Service
        google_plus_service = build('plus', 'v1', credentials=google_credentials)
        # Get the profile
        google_plus_profile = google_plus_service.people().get(userId='me').execute()
        # Create a user based on the id of the app user and store the google plus id
        google_plus_user = GooglePlusUserModel.get_or_insert(
            UserModel.get_by_id(users.get_current_user().user_id()).key.id(),
            credentials=google_credentials,
            google_plus_user_id=google_plus_profile['id']
        )
        google_plus_user.populate(credentials=google_credentials)
        google_plus_user.put()
        self.response.out.write('Success')