import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from models.auth import HumanAPIAuthModel
import humanapi

from config.config import get_api_keys

class HumanAPIAuthHandler(webapp2.RequestHandler):

    def get(self):
        self.redirect(self.get_auth_url())

    def get_auth_url(self):
        a = get_api_keys()
        auth = humanapi.Auth(
            client_id=get_api_keys().CLIENT_ID,
            client_secret=get_api_keys().CLIENT_SECRET,
            name='humanapi',
            authorize_url='https://user.humanapi.co/oauth/authorize',
            access_token_url='https://user.humanapi.co/oauth/token',
            base_url='https://api.humanapi.co/v1/human/')
        u = auth.get_authorize_url('localhost:8080/auth')
        return u