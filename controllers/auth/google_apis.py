import json
import webapp2

from webapp2 import uri_for
from config.config import get_client_secrets_filename


from oauth2client.client import flow_from_clientsecrets




class GoogleAuthHandler(webapp2.RequestHandler):
    def get_oauth2_flow(self):
        return flow_from_clientsecrets(
            get_client_secrets_filename(),
            scope='https://www.googleapis.com/auth/calendar',
            redirect_uri=self.request.host_url + uri_for('google_auth_callback')
        )
    pass


class GoogleAuthCallHandler(GoogleAuthHandler):

    def get(self):
        self.redirect(str(self.get_oauth2_flow().step1_get_authorize_url()))
        pass


class GoogleAuthCallbackHandler(GoogleAuthHandler):
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        runkeeper_auth_session = RunkeeperAuth(
            client_id=get_api_keys()['runkeeper']['client_id'],
            client_secret=get_api_keys()['runkeeper']['client_secret'],
            redirect_uri=self.request.host_url + uri_for('runkeeper_auth_callback')
        ).get_auth_session(
            code=self.request.get('code')
        )
        access_token = runkeeper_auth_session.access_token
        access_token_type = runkeeper_auth_session.token_response['token_type']

        runkeeper_api = RunkeeperAPI(
            access_token=access_token,
            access_token_type=access_token_type,
            debug=True
        )
        runkeeper_user = runkeeper_api.get_user()
        # test = runkeeper_user.call('')
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