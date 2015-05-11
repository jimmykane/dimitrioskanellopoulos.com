import sys
import logging
import json

from lib.logger import Logger
from apiclient.discovery import build


class GooglePlusAPI(object):
    # Set by init
    credentials = None
    google_plus_service = None
    debug_level = logging.DEBUG

    def __init__(self, credentials, debug=False):
        self.logger = Logger(
            'Google Plus API',
            logging.INFO if debug else logging.DEBUG
        )
        self.debug_level = logging.INFO if debug else logging.DEBUG
        self.credentials = credentials
        self.google_plus_service = build('plus', 'v1', credentials=credentials)

    def get_user(self):
        return GooglePlusUser(self)


class GooglePlusUser(object):

    _profile = None

    def __init__(self, master):
        self.master = master

    # Caches to instance
    @property
    def profile(self):
        self._profile = self._profile or self.get_profile()
        return self._profile

    # Also sets the profile
    def get_profile(self):
        self._profile = self.master.google_plus_service.people().get(userId='me').execute()
        return self._profile

    def latest_activity(self, collection='public'):
        return self.master.google_plus_service.activities().list(userId='me', collection=collection, maxResults='1').execute()
