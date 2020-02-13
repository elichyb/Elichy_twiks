import logging

class Log:
    def __init__(self, filename="bla.log"):
        self.logger = logging.getLogger('simple_example')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add the handlers to logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def info(self, message=""):
        self.logger.info(message)

    def debug(self, message=""):
        self.logger.debug(message)

    def error(self, message=""):
        self.logger.error(message)

    def warn(self, message=""):
        self.logger.warn(message)

    def critical(self, message=""):
        self.logger.critical(message)
        