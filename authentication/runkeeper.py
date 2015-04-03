import json

from rauth import OAuth2Service
from config.config import get_api_keys


class RunkeeperAuth(OAuth2Service):
    def __init__(self, client_id, client_secret):
        if (client_id or client_secret) is None:
            raise Exception('The client_id and client_secret are required')
        OAuth2Service.__init__(
            self,
            client_id=client_id,
            client_secret=client_secret,
            name='runkeeper',
            authorize_url=get_api_keys()['runkeeper']['urls']['authorization_url'],
            access_token_url=get_api_keys()['runkeeper']['urls']['access_token_url']
        )

    def get_authorize_url(self, redirect_uri):
        return super(RunkeeperAuth, self).get_authorize_url(
            response_type='code',
            redirect_uri=redirect_uri
        )

    def get_auth_session(self, code, redirect_uri, grant_type='authorization_code'):
        return super(RunkeeperAuth, self).get_auth_session(
            data={
                'grant_type': grant_type,
                'code': code,
                'redirect_uri': redirect_uri
            },
            decoder=json.loads
        )