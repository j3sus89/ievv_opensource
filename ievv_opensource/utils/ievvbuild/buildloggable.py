import logging


class BuildLoggable(object):
    def get_logger_name(self):
        raise NotImplementedError()

    def get_logger(self):
        return logging.getLogger(self.get_logger_name())
