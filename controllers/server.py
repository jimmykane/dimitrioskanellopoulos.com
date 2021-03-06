import os
import logging
import json

from models.users import UserModel, RunkeeperUserModel, GooglePlusUserModel
from config.config import is_dev_server


import webapp2
import jinja2
from google.appengine.api import users
from webapp2_extras.appengine.users import login_required
from google.appengine.api import memcache



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


class JSONReplyHandler(webapp2.RequestHandler):

    def json_dumps_response(self, response):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(response))

class MemcachedHandler(webapp2.RequestHandler):

    def get_cache_key(self, user_id, call, id_=None):
        return str(user_id) + str(call) + (id_ if id_ else '')

    def add_to_memcache(self, cache_key, data):
        # Only on production use cache
        if is_dev_server() and not self.request.get('clear_cache'):
            return True
        logging.debug('Writing to memcache key')
        return memcache.add(cache_key, data, 36000)

    def get_from_memcache(self, user_id, call, id_=None):
        return memcache.get(self.get_cache_key(user_id, call, id_))



class RootPageHandler(webapp2.RequestHandler):
    def get(self):
        jinja_environment = self.jinja_environment
        template = jinja_environment.get_template("/index.html")
        # Add vars and render
        self.response.out.write(template.render({
            "project": self.app.config['project'],
            "runkeeper_user_id": self.app.config['runkeeper_user_id'],
            "google_plus_user_id": self.app.config['google_plus_user_id']
        }))


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