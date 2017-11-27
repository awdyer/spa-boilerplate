import sys
import os
import logging

import falcon
import falcon_cors
from werkzeug.serving import run_simple

from web.config import config
from web.cognito import decode_jwt


logger = logging.getLogger()


def init_logging():
    for handler in logger.handlers:
        logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(config['logging']['format']))
    logger.addHandler(handler)
    logger.setLevel(config['logging']['level'])


class CatchAllHandler(Exception):
    @staticmethod
    def handle(ex, request, response, params):
        ''' Called if an exception has not been handled. Logs the exception. '''
        if isinstance(ex, falcon.HTTPError):
            # Don't log stack trace for request errors
            logger.info('{} ({}): {}'.format(ex.status, ex.description, request.url))
            raise ex

        logger.exception(ex)

        raise falcon.HTTPInternalServerError('Internal server error.',
            'An internal error occurred. If this problem persists, please contact us.')


class RootResource(object):
    def on_get(self, req, resp):
        '''GET / '''
        resp.body = 'Sup'


class ProtectedResource(object):
    def on_get(self, req, resp):
        '''GET /protected '''
        prefix, token = req.get_header('Authorization').split(' ')
        if prefix != 'Bearer:':
            raise falcon.HTTPBadRequest('Invalid authorization token.')

        claims = decode_jwt(token)
        logger.info(claims)
        resp.body = claims['username']


init_logging()

cors = falcon_cors.CORS(
    allow_origins_list=['http://localhost:8081', 'https://www.awdyer.com'],
    allow_all_headers=True,
    allow_all_methods=True
)

middleware = [
    cors.middleware
]

app = falcon.API(middleware=middleware)

app.add_route('/', RootResource())
app.add_route('/protected', ProtectedResource())

app.add_error_handler(Exception, CatchAllHandler.handle)


if __name__ == '__main__':
    # Program can be started with --dev flag log to auto reload when changes are made.
    dev = '--dev' in sys.argv
    if dev:
        # Workaround for the werkzeug reloader removing the current directory from the
        # path. It's nasty, but it works! Inspired by:
        # https://github.com/mitsuhiko/flask/issues/1246
        os.environ['PYTHONPATH'] = os.getcwd()

    # Listen for requests
    run_simple('localhost', 6001, app, use_reloader=dev)
