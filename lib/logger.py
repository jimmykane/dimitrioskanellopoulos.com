import sys
import logging


class Logger(object):
    def __init__(self, name, debug=False):
        if debug:
            self.level = logging.INFO
        else:
            self.level = logging.DEBUG

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler(sys.stderr))

    def log(self, *args, **kwargs):
        logging.log(self.level, *args, **kwargs)