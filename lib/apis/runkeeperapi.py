import sys
import logging
import json


from lib.logger import Logger
from google.appengine.api import urlfetch



class RunkeeperAPI(object):
    # Set by init
    access_token = None
    access_token_type = None

    runkeeper_api_root = 'https://api.runkeeper.com/'
    data_format = 'json'

    # Headers
    headers_content_type = 'application/x-www-form-urlencoded'
    headers_accept = 'application/vnd.com.runkeeper'

    def __init__(self, access_token, access_token_type, debug=False):
        self.logger = Logger(
            'Runkeeper API',
            logging.INFO if debug else logging.DEBUG
        )
        self.access_token = access_token
        self.access_token_type = access_token_type

    def _get_headers(self, call):
        return {
            'Content-Type': self.headers_content_type,
            'Accept': self.headers_accept + '.' + call + '+' + self.data_format,
            'Authorization': self.access_token_type + ' ' + self.access_token
        }

    def _query(self, call):
        result = urlfetch.fetch(
            # Can have some mapping or pattern
            url=call + '/',
            method=urlfetch.GET,
            # should add headers
            headers=self._get_headers(call)
        )
        if not result.status_code == 200:
            self.logger.log(self.level, result.content)
            return False
        return json.loads(result.content)


    @property
    def get_user(self, access_token_data):
        return self._query('user')
