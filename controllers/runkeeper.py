import logging
import urllib
import json

import webapp2


from google.appengine.api import urlfetch

from config.config import get_api_keys
from models.users import HumanAPIUser

class RunkeeperAuthHandler(object):

    pass

class RunkeeperAuthCallHandler(RunkeeperAuthHandler, webapp2.RequestHandler):

    def get(self):
        pass

class RunkeeperAuthCallBackHandler(RunkeeperAuthHandler, webapp2.RequestHandler):

    def get(self):
        pass