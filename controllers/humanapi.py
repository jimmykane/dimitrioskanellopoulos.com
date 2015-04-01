import logging
import urllib
import json

import webapp2


from google.appengine.api import urlfetch
from webapp2 import uri_for

from config.config import get_api_keys
from externalapis import humanapi as humanAPI
from models.users import HumanAPIUser

class HumanAPIAuthHandler(object):

    # Wrapper
    @classmethod
    def get_human_api(cls, access_token, debug=False):
        return humanAPI.HumanAPI(accessToken=access_token, debug=debug)

    @classmethod
    def get_humanapi_auth(cls):
         return humanAPI.Auth(
            client_id=get_api_keys()['humanapi']['client_id'],
            client_secret=get_api_keys()['humanapi']['client_secret'])


class HumanAPIAuthCallHandler(HumanAPIAuthHandler, webapp2.RequestHandler):

    def get(self):
        self.redirect(self.get_humanapi_auth().get_authorize_url(uri_for('humanapi_auth_callback')))


class HumanAPIAuthCallBackHandler(HumanAPIAuthHandler, webapp2.RequestHandler):

    def get(self):
        if not self.request.get('code'):
            self.response.out.write('Error')
            return

        # Get the auth session
        humanapi_session = self.get_humanapi_auth().get_auth_session(self.request.get('code'))

        # Get the API
        users_humanapi = self.get_human_api(humanapi_session.access_token)

        # Get the profile
        users_humanapi_profile = users_humanapi.profile.get()
        users_humanapi_human = users_humanapi.human.get()
        users_humanapi_activities = users_humanapi.activity.list()

        result = urlfetch.fetch(
            url='https://user.humanapi.co/v1/connect/publictokens',
            payload=json.dumps({
                'humanId': users_humanapi_profile['humanId'],
                'clientId': get_api_keys()['humanapi']['client_id'],
                'clientSecret': get_api_keys()['humanapi']['client_secret'],
            }),
            method=urlfetch.POST,
            headers={'Content-Type': 'application/json'}
        )

        if result.status_code != 200:
            self.response.out.write('Error')

        # Create a or retrieve the user
        humanapi_user = HumanAPIUser.get_or_insert(
            users_humanapi_profile['userId'],
            email=users_humanapi_profile['email'],
            human_id=users_humanapi_profile['humanId'],
            access_token=humanapi_session.access_token,
            access_token_key=humanapi_session.access_token_key,
            public_token=json.loads(result.content)['publicToken']
        )

        # Update the user with new tokens if needed @todo check object
        humanapi_user.populate(
            email=users_humanapi_profile['email'],
            human_id=users_humanapi_profile['humanId'],
            access_token=humanapi_session.access_token,
            access_token_key=humanapi_session.access_token_key,
            public_token=json.loads(result.content)['publicToken']
        )
        humanapi_user.put()

        pass