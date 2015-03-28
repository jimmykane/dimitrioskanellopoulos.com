import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from config.config import get_api_keys
from externalapis import humanapi
from webapp2 import uri_for

class HumanAPIAuthHandler(object):

    @classmethod
    def get_humanapi_auth(self):
         return humanapi.Auth(
            client_id=get_api_keys()['humanapi']['client_id'],
            client_secret=get_api_keys()['humanapi']['client_secret'])


class HumanAPIAuthCallHandler(HumanAPIAuthHandler, webapp2.RequestHandler):

    def get(self):
        self.redirect(self.get_humanapi_auth().get_authorize_url('http://localhost:8080/auth/humanapi_auth_callback'))


class HumanAPIAuthCallBackHandler(webapp2.RequestHandler):

    def get(self):
        pass