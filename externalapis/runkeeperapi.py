import logging
import json

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

    def __init__(self, access_token=None, access_token_type=None, debug=False):
        if debug:
            self.level = logging.INFO
        else:
            self.level = logging.DEBUG

    def _get_headers(self, call):
        return {
            'Content-Type': self.headers_content_type,
            'Accept': self.headers_accept + '.' + call + '+' + self.data_format,
            'Authorization': self.access_token_type + ' ' + self.access_token
        }


    @property
    def get_user(self, access_token_data):
            result = urlfetch.fetch(
                url='user/',
                method=urlfetch.GET,
                #should add headers
            )
            if not result.status_code == 200:
                self.request.response.out.write(result.content)
                return False
            return json.loads(result.content)