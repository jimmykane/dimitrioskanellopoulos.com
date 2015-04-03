from rauth import OAuth2Service
from config.config import get_api_keys

class Auth(OAuth2Service):
    def __init__(self, client_id, client_secret):
        if client_id is None:
            raise Exception('The HumanAPI client_id and client_secret are required')
        else:
            print "client id " + client_id
        if client_secret is None:
            raise Exception('The HumanAPI client_id and client_secret are required')
        else:
            print "client secret " + client_secret
        OAuth2Service.__init__(self,
            client_id=client_id,
            client_secret=client_secret,
            name='humanapi',
            authorize_url='https://user.humanapi.co/oauth/authorize',
            access_token_url='https://user.humanapi.co/oauth/token',
            base_url='https://api.humanapi.co/v1/human/')

    def get_authorize_url(self, redirect_uri):
        return super(Auth, self).get_authorize_url(
            response_type='code',
            redirect_uri=redirect_uri,
            # Optional
            # user='user@email.com',
            # mode='edit' #for editing streams instead of first time grants
        )

    def get_edit_url(self, redirect_uri):
        return super(Auth, self).get_authorize_url(
            response_type='code',
            redirect_uri=redirect_uri,
            # Optional
            # user='user@email.com',
            mode='edit' #for editing streams instead of first time grants
        )

    def get_auth_session(self, code, scope=''):
        return super(Auth, self).get_auth_session(data={
            'scope': scope,
            'code': code,
        }, decoder=json.loads)