import logging
import logging.handlers

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam3.log')
fh.setLevel(logging.INFO)
fh2 = logging.FileHandler('spam2.log')
fh2.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
formatter2 = logging.Formatter('%(asctime)s-%(threadName)s-%(levelname)s-%(message)s')
handler = logging.handlers.RotatingFileHandler('spam.log',maxBytes=1024000, backupCount=5)
th = logging.handlers.TimedRotatingFileHandler('timespam.log',when='S',interval=10,backupCount=5)
fh.setFormatter(formatter)
fh2.setFormatter(formatter2)
handler.setFormatter(formatter)
th.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(fh2)
logger.addHandler(ch)
logger.addHandler(handler)
logger.addHandler(th)


logger.info('creating an instance of auxiliary_module.Auxiliary')
logger.error('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
logger.debug('finished auxiliary_module.Auxiliary.do_something')
logger.warning('calling auxiliary_module.some_function()')
for s in range(100):
    logger.info('This is message %d'%s)
logger.info('done with auxiliary_module.some_function()')
logger.info('---------------------\r\n')
