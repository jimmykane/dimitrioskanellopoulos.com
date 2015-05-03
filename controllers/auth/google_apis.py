import webapp2
import pickle,json

from webapp2 import uri_for
from config.config import get_client_secrets_filename
from apiclient.discovery import build

from oauth2client.client import flow_from_clientsecrets
from webapp2_extras.appengine.users import login_required




class GoogleAuthHandler(webapp2.RequestHandler):
    def get_oauth2_flow(self, scope=None):
        return flow_from_clientsecrets(
            get_client_secrets_filename(),
            # Should use the above var but now is off due to sec concerns
            scope='https://www.googleapis.com/auth/plus.login',
            redirect_uri=self.request.host_url + uri_for('google_auth_callback')
        )
    pass


class GoogleAuthCallHandler(GoogleAuthHandler):

    @login_required
    def get(self, scope):
        self.redirect(str(self.get_oauth2_flow().step1_get_authorize_url()))
        pass


class GoogleAuthCallbackHandler(GoogleAuthHandler):
    @login_required
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        google_credentials = self.get_oauth2_flow().step2_exchange(self.request.params.get('code'))
        service = build('plus', 'v1', credentials=google_credentials)
        googleplus_profile = service.people().get(userId='me').execute()
        self.response.out.write('Success')