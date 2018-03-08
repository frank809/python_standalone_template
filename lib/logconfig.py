import logging
import logging.handlers
import sys


# create logger with
logger = logging.getLogger()
logger.setLevel(logging.NOTSET)


def initlog(logname,level=logging.INFO):
    # create file handler which logs even debug messages
    filehandler = logging.handlers.RotatingFileHandler(logname, maxBytes=1024 * 1024, backupCount=5)
    filehandler.setLevel(level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(module)s:%(lineno)d|%(message)s')
    filehandler.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(filehandler)

initlog(logname="Appname")