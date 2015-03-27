import os

import webapp2
import jinja2


class RootPage(webapp2.RequestHandler):
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