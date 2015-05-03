import logging

from models.users import UserModel

import webapp2
from google.appengine.api import users
from webapp2_extras.appengine.users import login_required


class LoginHandler(webapp2.RequestHandler):

    @login_required
    def get(self):
        user = users.get_current_user()
        user = UserModel.get_or_insert(user.user_id())
    pass


class LogoutHandler(webapp2.RequestHandler):

    def get(self):
        try:
            return self.redirect(users.create_logout_url('/'))
        except Exception as e:
            logging.exception('Could not Logout user\n' + repr(e))
            self.redirect('/')
            return