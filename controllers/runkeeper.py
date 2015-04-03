import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from webapp2 import uri_for


from config.config import get_api_keys
from models.users import RunkeeperUser
from authentication import runkeeper

class RunkeeperAuthHandler(object):
    pass


class RunkeeperAuthCallHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        self.redirect(str(self.get_auth_url()))

    def get_auth_url(self):
        return \
            get_api_keys()['runkeeper']['urls']['authorization_url'] \
            + '?' \
            + 'client_id=' + get_api_keys()['runkeeper']['client_id'] \
            + '&' \
            + 'response_type=code' \
            + '&' \
            + 'redirect_uri=' + self.request.host_url + uri_for('runkeeper_auth_callback')


class RunkeeperAuthCallbackHandler(RunkeeperAuthHandler, webapp2.RequestHandler):
    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if self.request.params.get('code'):
            access_token_data = self.request_access_token(code=self.request.params.get('code'))
            if not access_token_data:
                return
            # Get or insert the model update tokens etc
            runkeeper_auth_model = RunkeeperUser.get_or_insert(
                str(self.get_user_id(access_token_data)['userID']),
                access_token=access_token_data['access_token'],
                token_type=access_token_data['token_type']
            )
            runkeeper_auth_model.populate(
                access_token=access_token_data['access_token'],
                token_type=access_token_data['token_type']
            )
            runkeeper_auth_model.put()
            # Write the result
            self.response.out.write('Success')

    def get_user_id(self, access_token_data):
        result = urlfetch.fetch(
            url='https://api.runkeeper.com/user/',
            method=urlfetch.GET,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/vnd.com.runkeeper.User+json',
                'Authorization': access_token_data['token_type'] + ' ' + access_token_data['access_token']
            }
        )
        if not result.status_code == 200:
            self.request.response.out.write(result.content)
            return False
        return json.loads(result.content)

    def request_access_token(self, code):
        result = urlfetch.fetch(
            url=get_api_keys()['runkeeper']['urls']['access_token_url'],
            payload=urllib.urlencode({
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': get_api_keys()['runkeeper']['client_id'],
                'client_secret': get_api_keys()['runkeeper']['client_secret'],
                'redirect_uri': self.request.host_url + uri_for('runkeeper_auth_callback')
            }),
            method=urlfetch.POST,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        if not result.status_code == 200:
            self.request.response.out.write(result.content)
            return False

        # Should check for error
        return json.loads(result.content)