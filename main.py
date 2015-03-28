import logging
from controllers import server, humanapi, metrics
from config import config
import webapp2


app = webapp2.WSGIApplication(
    [
        # Essential handlers
        ('/', server.RootPage),

        # Human API  handlers
        ('/auth/humanapi_auth', humanapi.HumanAPIAuthHandler),

    ], debug=True, config=config.config)


# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! Naughty Mr. Jiggles (This is a 404)')
    response.set_status(404)

app.error_handlers[404] = handle_404
