import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from webapp2 import uri_for

from config.config import get_api_keys
from models.users import RunkeeperUser
from externalapis.runkeeperapi import RunkeeperAPI

class RunkeeperAuthHandler(object):
    @classmethod
    def get_runkeeper_auth(cls):
        return RunkeeperAuth(
            client_id=get_api_keys()['runkeeper']['client_id'],
            client_secret=get_api_keys()['runkeeper']['client_secret']
        )


class RunkeeperAuthCallHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        self.redirect(self.get_runkeeper_auth().get_authorize_url(self.request.host_url + uri_for('runkeeper_auth_callback')))


class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if not self.request.params.get('code'):
            return
        # Get the auth session
        runkeeper_auth_session = self.get_runkeeper_auth().get_auth_session(self.request.get('code'), self.request.host_url + uri_for('runkeeper_auth_callback'))

        runkeeper_api = RunkeeperAPI(access_token=runkeeper_auth_session.access_token, access_token_type='', debug=True)
        # Get or insert the model update tokens etc
        pass
        runkeeper_auth_model = RunkeeperUser.get_or_insert(
            str(self.get_user_id(access_token_data)['userID']),
            access_token=access_token_data['access_token'],
            token_type=access_token_data['token_type']
        )
        runkeeper_auth_model.populate(
            access_token=access_token_data['access_token'],
            token_type=access_token_data['token_type']
        )
        runkeeper_auth_model.put()
        # Write the result
        self.response.out.write('Success')