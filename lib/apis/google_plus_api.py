import sys
import logging
import json

from lib.logger import Logger


class GooglePlusAPI(object):
    # Set by init
    credentials = None
    debug_level = logging.DEBUG

    def __init__(self, credentials, debug=False):
        self.logger = Logger(
            'Google Plus API',
            logging.INFO if debug else logging.DEBUG
        )
        self.debug_level = logging.INFO if debug else logging.DEBUG
        self.credentials = credentials

    def get_user(self):
        return GooglePlusUser(self)


class GooglePlusUser(object):
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