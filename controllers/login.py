from models.users import UserModel

import webapp2
from google.appengine.api import users



class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri), abort=True)
            return

        user = UserModel.get_or_insert(user.user_id())
    pass