import json

import webapp2


class JSONReplyHandler(webapp2.RequestHandler):

    def json_dumps_response(self, response):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(response))