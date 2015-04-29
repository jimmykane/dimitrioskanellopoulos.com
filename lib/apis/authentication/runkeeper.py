import json

from oauth2client.client import OAuth2WebServerFlow
from config.config import get_api_keys


class RunkeeperAuth(object):
    def __init__(self, client_id, client_secret, redirect_uri):
        if (client_id or client_secret or redirect_uri) is None:
            raise Exception('The client_id and client_secret are required')
        self.flow = OAuth2WebServerFlow(
            client_id=client_id,
            client_secret=client_secret,
            scope='',
            redirect_uri=redirect_uri,
            user_agent=None,
            auth_uri=str(get_api_keys()['runkeeper']['urls']['authorization_url']),
            token_uri=str(get_api_keys()['runkeeper']['urls']['access_token_url']),
            revoke_uri=None
        )

    def get_authorize_url(self):
        return self.flow.step1_get_authorize_url()

    def get_auth_session(self, code):
        return self.flow.step2_exchange(code=code)