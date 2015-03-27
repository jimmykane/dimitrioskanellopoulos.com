import logging
from controllers import server, auth, metrics
from config import config
import webapp2


app = webapp2.WSGIApplication(
    [
        # Essential handlers
        ('/', server.RootPage),

        # Auth handlers
        ('/auth/runkeeper', auth.RunkeeperAuthHandler),
        ('/auth/runkeeper_callback', auth.RunkeeperAuthCallbackHandler),


        # Metrics handlers /metrics/(service)/(user)/(action)
        (r'/metrics/runkeeper/(.*)/(.*)', metrics.RunkeeperMetricsHandler),

    ], debug=True, config=config.config)


# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! Naughty Mr. Jiggles (This is a 404)')
    response.set_status(404)

app.error_handlers[404] = handle_404
