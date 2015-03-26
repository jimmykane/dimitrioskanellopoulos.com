import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from google.appengine.ext import ndb
from models.auth import RunkeeperAuthModel


class AuthHandler(webapp2.RequestHandler):
    pass

    def get_auth_url(self):
        raise NotImplementedError


class AuthCallbackHandler(webapp2.RequestHandler):
    pass

    def request_access_token(self, code):
        raise NotImplementedError


class RunkeeperAuthHandler(AuthHandler):

    def get(self):
        self.redirect(self.get_auth_url())

    def get_auth_url(self):
        return\
            self.app.config['project']['api_keys']['runkeeper']['urls']['authorization_url'] \
            + '?' \
            + 'client_id=' + self.app.config['project']['api_keys']['runkeeper']['client_id'] \
            + '&' \
            + 'response_type=code' \
            + '&' \
            + 'redirect_uri=' + self.app.config['project']['api_keys']['runkeeper']['urls']['redirect_uri']


class RunkeeperAuthCallbackHandler(AuthCallbackHandler):

    def get(self):
        if self.request.params.get('error'):
            self.request.response.out.write(self.request.params.get('error'))
            return

        if self.request.params.get('code'):
            access_token_data = self.request_access_token(code=self.request.params.get('code'))
            if not access_token_data:
                return
            # Now lets request the user to do a get or insert and have a key
            RunkeeperAuthModel(
                access_token=access_token_data['access_token'],
                token_type=access_token_data['token_type']
            )
            RunkeeperAuthModel.get_or_insert(
                str(self.get_user_id(access_token_data)['userID']),
                access_token=access_token_data['access_token'],
                token_type=access_token_data['token_type']
            ).put()
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
            url=self.app.config['project']['api_keys']['runkeeper']['urls']['access_token_url'],
            payload= urllib.urlencode({
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': self.app.config['project']['api_keys']['runkeeper']['client_id'],
                'client_secret': self.app.config['project']['api_keys']['runkeeper']['client_secret'],
                'redirect_uri': self.app.config['project']['api_keys']['runkeeper']['urls']['redirect_uri']
            }),
            method=urlfetch.POST,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        if not result.status_code == 200:
            self.request.response.out.write(result.content)
            return False

        # Should check for error
        return json.loads(result.content)