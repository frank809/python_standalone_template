from lib import logger
import lib
import sys


logger.error('param:%s', sys.argv[0])


logger.error('Hello')
logger.info('creating an instance of auxiliary_module.Auxiliary')
logger.error('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
logger.debug('finished auxiliary_module--989-')
logger.warning('calling auxiliary_module.some_function()')
for s in range(1):
    logger.info('This is message %d'%s)
logger.info('done with auxiliary_module.some_function()')
logger.debug('This is debug log.')
logger.info('---------------------\r\n')

def test():
    logger.error('Shuo dian sha hao ne?')
    return
def hi():
    test()
    return

print "1"

