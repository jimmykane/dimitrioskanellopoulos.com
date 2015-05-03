import os
import logging

from models.users import UserModel

import webapp2
import jinja2
from google.appengine.api import users
from webapp2_extras.appengine.users import login_required


"""
A decorator to wrap the login_required decorator
"""
def register_required(handler_method):
    @login_required
    def check_register(self, *args, **kwargs):
        if not UserModel.get_or_insert(users.get_current_user().user_id()):
            logging.error('Could not register user')
            return
        handler_method(self, *args, **kwargs)

    return check_register


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


class LogoutHandler(webapp2.RequestHandler):

    @register_required
    def get(self):
        try:
            return self.redirect(users.create_logout_url('/'))
        except Exception as e:
            logging.exception('Could not Logout user\n' + repr(e))
            self.redirect('/')
            return