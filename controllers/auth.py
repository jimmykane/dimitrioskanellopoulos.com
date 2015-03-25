import logging
import urllib
import json

import webapp2

from google.appengine.api import urlfetch
from models.auth import RunkeeperAuth


class AutRunkeeperhHandler(webapp2.RequestHandler):

    def get(self):
        self.redirect(self._get_auth_url())

    def _get_auth_url(self):
        return\
            self.app.config['project']['api_keys']['runkeeper']['urls']['authorization_url'] \
            + '?' \
            + 'client_id=' + self.app.config['project']['api_keys']['runkeeper']['client_id'] \
            + '&' \
            + 'response_type=code' \
            + '&' \
            + 'redirect_uri=' + self.app.config['project']['api_keys']['runkeeper']['urls']['redirect_uri']


class AuthRunkeeperCallbackHandler(webapp2.RequestHandler):

    def get(self):
        if self.request.params.get('error') == 'access_denied':
            self.request.response.out.write(self.request.params.get('error'))
            return
        if self.request.params.get('code'):
            # Should make dummy request  to validate auth
            runkeeper_auth = RunkeeperAuth()
            runkeeper_auth.code = self.request.params.get('code')
            # Should do get or insert
            runkeeper_auth.put()
            access_token = self._get_access_token()
            if not access_token:
                return

            logging.info(access_token)




    def _get_access_token(self):
        result = urlfetch.fetch(
            url=self.app.config['project']['api_keys']['runkeeper']['urls']['access_token_url'],
            payload= urllib.urlencode({
                'grant_type': 'authorization_code',
                'code': self.request.params.get('code'),
                'client_id': self.app.config['project']['api_keys']['runkeeper']['client_id'],
                'client_secret': self.app.config['project']['api_keys']['runkeeper']['client_secret'],
                'redirect_uri': self.app.config['project']['api_keys']['runkeeper']['urls']['redirect_uri']
            }),
            method=urlfetch.POST,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        logging.info(result.content)
        if not (result.status_code == 200):
            return False

        # Should check for error
        return json.dumps(result.content)