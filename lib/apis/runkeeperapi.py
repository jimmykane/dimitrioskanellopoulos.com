import sys
import logging
import json

from lib.logger import Logger
from google.appengine.api import urlfetch


class RunkeeperAPI(object):
    # Set by init
    access_token = None
    access_token_type = None
    debug_level = logging.DEBUG

    runkeeper_api_root = 'https://api.runkeeper.com/'
    data_format = 'json'

    # Headers
    headers_content_type = 'application/vnd.com.runkeeper'
    headers_accept = 'application/vnd.com.runkeeper'

    def __init__(self, access_token, access_token_type, debug=False):
        self.logger = Logger(
            'Runkeeper API',
            logging.INFO if debug else logging.DEBUG
        )
        self.debug_level = logging.INFO if debug else logging.DEBUG
        self.access_token = access_token
        self.access_token_type = access_token_type

    def _get_headers(self, call):
        return {
            'Content-Type': self.headers_accept + '.' + call + '+' + self.data_format,
            #'Accept': self.headers_accept + '.' + call + '+' + self.data_format,
            'Authorization': self.access_token_type + ' ' + self.access_token
        }

    def query(self, call):
        result = urlfetch.fetch(
            # Can have some mapping or pattern
            url=self.runkeeper_api_root + '/' + call ,
            method=urlfetch.GET,
            # should add headers
            headers=self._get_headers(call)
        )
        if not result.status_code == 200:
            # Byuggy @todo kill
            # self.logger.log(self.debug_level, str(result.content))
            return False
        return json.loads(result.content)

    def get_user(self):
        # @todo create the following properties from the user iteratable
        # Should return user
        return RunkeeperUser(self)

class RunkeeperUser(object):

    user_id = None

    def __init__(self, master):
        self.master = master
        # Get the user methods and set the attributes
        b= self.master.query('user')
        for user_method, call in self.master.query('user').iteritems():
            if user_method == 'userID':
                # Assign the userID to the object
                self.user_id = call
                continue
            # Should not get the value but bind a method
            setattr(
                self,
                user_method,
                lambda call=call: self.master.query(call)
            )

    def get_user_id(self):
        return self.user_id