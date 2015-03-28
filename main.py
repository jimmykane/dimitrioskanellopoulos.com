import logging
from controllers import server, humanapi, metrics
from config import config
import webapp2


app = webapp2.WSGIApplication(
    [
        # Essential handlers
        webapp2.Route('/', handler=server.RootPage),

        # Human API  handlers
        webapp2.Route('/auth/humanapi_auth_call', handler=humanapi.HumanAPIAuthCallHandler, name='humanapi_auth_call'),
        webapp2.Route('/auth/humanapi_auth_callback', handler=humanapi.HumanAPIAuthCallBackHandler, name='humanapi_auth_callback'),

    ], debug=True, config=config.config)


# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! Naughty Mr. Jiggles (This is a 404)')
    response.set_status(404)

app.error_handlers[404] = handle_404
