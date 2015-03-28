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
        auth_session = self.get_humanapi_auth().get_auth_session(self.request.get('code'))
        UserHumanAPI = self.get_human_api(auth_session.access_token)
        user_humanapi_profile = UserHumanAPI.profile.get()
        HumanAPIUser.get_or_insert(
            user_humanapi_profile['userId'],
            email=user_humanapi_profile['email'],
            human_id=user_humanapi_profile['humanId'],
            access_token=auth_session.access_token,
            access_token_key=auth_session.access_token_key
        )

        pass