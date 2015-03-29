import logging
import urllib
import json

import webapp2


from google.appengine.api import urlfetch
from webapp2 import uri_for

from config.config import get_api_keys
from externalapis import humanapi as humanAPI
from models.users import HumanAPIUser

class HumanAPIAuthHandler(object):

    # Wrapper
    @classmethod
    def get_human_api(cls, access_token, debug=False):
        return humanAPI.HumanAPI(accessToken=access_token, debug=debug)

    @classmethod
    def get_humanapi_auth(cls):
         return humanAPI.Auth(
            client_id=get_api_keys()['humanapi']['client_id'],
            client_secret=get_api_keys()['humanapi']['client_secret'])


class HumanAPIAuthCallHandler(HumanAPIAuthHandler, webapp2.RequestHandler):

    def get(self):
        self.redirect(self.get_humanapi_auth().get_authorize_url('http://localhost:8080/auth/humanapi_auth_callback'))


class HumanAPIAuthCallBackHandler(HumanAPIAuthHandler, webapp2.RequestHandler):

    def get(self):
        if not self.request.get('code'):
            self.response.out.write('Error')
            return

        # Get the auth session
        humanapi_session = self.get_humanapi_auth().get_auth_session(self.request.get('code'), scope='')

        # Get the API
        users_humanapi = self.get_human_api(humanapi_session.access_token)

        # Get the profile
        users_humanapi_profile = users_humanapi.profile.get()

        # Create a or retrieve the user
        humanapi_user = HumanAPIUser.get_or_insert(
            users_humanapi_profile['userId'],
            email=users_humanapi_profile['email'],
            human_id=users_humanapi_profile['humanId'],
            access_token=humanapi_session.access_token,
            access_token_key=humanapi_session.access_token_key
        )

        # Update the user with new tokens
        humanapi_user.populate(access_token=humanapi_session.access_token, access_token_key=humanapi_session.access_token_key)
        humanapi_user.put()

        pass