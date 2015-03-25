'''
@author: Dimitrios Kanellopoulos
@contact: jimmykane9@gmail.com
'''
import os
import re
import logging
import config
import json

import webapp2
import jinja2

from google.appengine.ext import ndb


class RootPage(webapp2.RequestHandler):
    def get(self):
        jinja_environment = self.jinja_environment
        template = jinja_environment.get_template("/index.html")
        # Add analytics and render template
        self.response.out.write(template.render({"project": self.app.config.get('project')}))


    @property
    def jinja_environment(self):
        jinja_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__),
                             '../views'
                ))
        )
        return jinja_environment