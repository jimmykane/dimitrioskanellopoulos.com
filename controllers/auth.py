import logging
import urllib2
import urllib

import webapp2

from models.auth import RunkeeperAuth


class RunkeeperAuthHandler(webapp2.RequestHandler):

    def get(self):
        try:
            self.redirect(self._get_auth_url())
        except urllib2.URLError, e:
            logging.error(e.message)
            pass
        return

    def _get_auth_url(self):
        return\
            self.app.config['project']['api_keys']['runkeeper']['urls']['authorization_url'] \
            + '?' \
            + 'client_id=' + self.app.config['project']['api_keys']['runkeeper']['client_id'] \
            + '&' \
            + 'response_type=code' \
            + '&' \
            + 'redirect_uri=' + self.app.config['project']['api_keys']['runkeeper']['urls']['redirect_uri']


class RunkeeperAuthCallbackHandler(webapp2.RequestHandler):

    def get(self):
        if self.request.params.get('error') == 'access_denied':
            self.request.response.out.write(self.request.params.get('error'))
            return
        if not self.request.params.get('code'):
            self.request.response.out.write('No code')
            return
        # Should make dummy request  to validate auth
        runkeeper_auth = RunkeeperAuth()
        runkeeper_auth.code = self.request.params.get('code')
        # Should do get or insert
        runkeeper_auth.put()