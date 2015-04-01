import logging
import urllib
import json

import webapp2


from google.appengine.api import urlfetch

from config.config import get_api_keys

class RunkeeperAuthHandler(object):

    pass

class RunkeeperAuthCallHandler(RunkeeperAuthHandler, webapp2.RequestHandler):

    def get(self):
        pass

class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler, webapp2.RequestHandler):

    def get(self):
        pass