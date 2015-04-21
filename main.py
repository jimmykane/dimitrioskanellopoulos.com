import logging

from controllers import server, runkeeper, metrics
from config import config

import webapp2


app = webapp2.WSGIApplication(
    [
        # Essential handlers
        webapp2.Route(
            '/',
            handler=server.RootPage
        ),

        # Runkeeper API Auth handlers
        webapp2.Route(
            '/auth/runkeeper_auth_call',
            handler=runkeeper.RunkeeperAuthCallHandler,
            name='runkeeper_auth_call'
        ),
        webapp2.Route(
            '/auth/runkeeper_auth_callback',
            handler=runkeeper.RunkeeperAuthCallbackHandler,
            name='runkeeper_auth_callback'
        ),

        # Metrics
        webapp2.Route(
            r'/metrics/runkeeper/<user_id:\d+>/<call:\w+>',
            handler=metrics.RunkeeperMetricsHandler,
            name='runkeeper_metrics'
        ),
        webapp2.Route(
            r'/metrics/runkeeper/<user_id:\d+>/<call:\w+>/<id_:\d+>',
            handler=metrics.RunkeeperMetricsHandler,
            name='runkeeper_metrics'
        ),

    ], debug=True, config=config.config)


# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! Naughty Mr. Jiggles (This is a 404)')
    response.set_status(404)


app.error_handlers[404] = handle_404
