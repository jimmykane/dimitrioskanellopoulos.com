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

    def __init__(self, master):
        self.master = master

    @property
    def user_id(self):
        return self.master.google_plus_service.people().get(userId='me').execute()['id']

    def get_profile(self):
        return self.master.google_plus_service.people().get(userId='me').execute()

    def list_activities(self, collection='public', max_results=20):
        return self.master.google_plus_service.activities().list(userId='me', collection=collection, maxResults=max_results).execute()['items']

    def get_latest_activity(self, collection='public'):
        return self.list_activities(collection=collection, max_results=1)