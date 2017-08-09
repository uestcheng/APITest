import logging


class Logger(object):
    """Logger class doing two things
       1. print out to the console
       2. loggin to the file in the output

    """

    def __init__(self, log_level, way='print'):
        self.fmt = "%(asctime)s-%(levelname)s: %(name)s-%(message)s"
        self.way = way
        self.level = log_level
        self.level_type = ("DEBUG", "CRITICAL", "WARNING")

    def _info_log(self, msg):
        """log common info of test"""
        logging.basicConfig(self.fmt)
        getattr(logging, "debug")(msg)

    def _error_log(self, msg):
        """log error info of test"""
        logging.basicConfig(self.fmt)
        getattr(logging, "warning")(msg)

    def logger(self, level, msg):
        if level in self.level_type:
            self._info_log(msg)
        else:
            self._error_log(msg)
