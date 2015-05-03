import os
import logging

from models.users import UserModel

import webapp2
import jinja2
from google.appengine.api import users
from webapp2_extras.appengine.users import login_required

class RootPageHandler(webapp2.RequestHandler):
    def get(self):
        jinja_environment = self.jinja_environment
        template = jinja_environment.get_template("/index.html")
        # Add analytics and render template
        self.response.out.write(template.render({"project": self.app.config['project']}))


    @property
    def jinja_environment(self):
        jinja_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__),
                             '../templates'
                             ))
        )
        return jinja_environment


class LoginHandler(webapp2.RequestHandler):

    @login_required
    def get(self):
        user = UserModel.get_or_insert(users.get_current_user().user_id())


class LogoutHandler(webapp2.RequestHandler):

    def get(self):
        try:
            return self.redirect(users.create_logout_url('/'))
        except Exception as e:
            logging.exception('Could not Logout user\n' + repr(e))
            self.redirect('/')
            return