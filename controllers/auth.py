import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from models.auth import HumanAPIAuthModel
from humanapi import get_authorize_url, get_auth_session

class AuthHandler(webapp2.RequestHandler):
    pass

    def get_auth_url(self):
        raise NotImplementedError


class AuthCallbackHandler(webapp2.RequestHandler):
    pass

    def request_access_token(self, code):
        raise NotImplementedError