import json

from config.config import is_dev_server

import webapp2
from google.appengine.api import memcache
from oauth2client.appengine import OAuth2DecoratorFromClientSecrets


decorator = OAuth2DecoratorFromClientSecrets(
    'client_secrets.json',
    scope='https://www.googleapis.com/auth/calendar')


class GooglePlusAPIHandler(webapp2.RequestHandler):
    # @todo implement this better with auth scopes...
    disallowed_calls = [

    ]

    def get(self, user_id, call, id_=None):
        # If its not allowed gto
        if not is_dev_server() and call in self.disallowed_calls:
            self.response.out.write('Call not allowed')
            return
