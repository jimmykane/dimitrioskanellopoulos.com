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