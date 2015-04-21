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

    runkeeper_api_root = 'https://api.runkeeper.com'
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
            # 'Accept': self.headers_accept + '.' + call + '+' + self.data_format,
            'Authorization': self.access_token_type + ' ' + self.access_token
        }

    def query(self, call, id_=None):
        urlfetch.set_default_fetch_deadline(60)
        result = urlfetch.fetch(
            # Can have some mapping or pattern
            url=self.runkeeper_api_root + call + ('/' + id_ if id_ else ''),
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
        for user_method, call in self.master.query('/user').iteritems():
            if user_method == 'userID':
                # Assign the userID to the object
                self.user_id = call
                continue
            # add them also with the camelcase
            setattr(
                self,
                call[1:],
                lambda id_=None, _call=call: self.master.query(_call, id_)
            )

        # Set the other attributes
        # @todo feels this should be elsewhere
        setattr(self, 'weightMeasurements', self.get_weight_measurements)
        setattr(self, 'latestActivity', self.get_latest_activity)

    def get_user_id(self):
        return self.user_id

    """
    Wrapper to pass the latest and save data
    """

    def get_latest_activity(self):
        return self.fitnessActivities()['items'][0]

    """
    Wrapper to do partial logic and save data
    """

    def get_weight_measurements(self):
        weight = None
        fat_percent = None
        # @todo optimize
        for item in self.weight()['items']:
            if not weight:
                weight = item.get('weight')
            if not fat_percent:
                fat_percent = item.get('fat_percent')
        return {
            'weight': weight,
            'fat_percent': fat_percent
        }