import logging

import webapp2

from controllers import server, runkeeper, metrics, apis
from controllers.auth import google_apis
from config import config


app = webapp2.WSGIApplication(
    [
        # Essential handlers
        webapp2.Route(
            '/',
            handler=server.RootPage
        ),

        # Authentication Google
        webapp2.Route(
            '/auth/google_auth_call',
            handler=google_apis.GoogleAuthCallHandler,
            name='google_auth_callback'
        ),
        webapp2.Route(
            '/auth/google_auth_callback',
            handler=google_apis.GoogleAuthCallbackHandler,
            name='google_auth_callback'
        ),

        # Authentication Runkeeper

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

        # Metrics Runkeeper
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

        # Google+ API
        webapp2.Route(
            r'/apis/google+/<user_id:\d+>/<call:\w+>/<id_:\d+>',
            handler=apis.GooglePlusAPIHandler,
            name='google+_api'
        ),

    ], debug=True, config=config.config)


# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! Naughty Mr. Jiggles (This is a 404)')
    response.set_status(404)


app.error_handlers[404] = handle_404
