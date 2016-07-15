import logging
# import sys
# 
# 
# 
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# root = logging.getLogger()
# ch = logging.StreamHandler(sys.stdout)
# root.addHandler(ch)
# 
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.warning('%s before you %s', 'Look', 'leap!')


# import logging
# logging.warning('%s before you %s', 'Look', 'leap!')
# logging.warning('And this, too')

# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s',filename='example.log',  filemode='w', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

# import logging
# import sys
# logging.basicConfig(format='%(levelname)s:%(name)s  %(message)s %(asctime)s')
# root = logging.getLogger()
# 
# # root.addHandler(logging.StreamHandler(sys.stdout))
# ch = logging.FileHandler('example.log', mode='w')
# ch.setFormatter(logging.Formatter('%(levelname)s:%(name)s  %(message)s %(asctime)s')) 
# ch.setLevel(logging.DEBUG)
# root.addHandler(ch )
# # logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s  %(message)s %(asctime)s')
# 
# 
import sys
_logger = logging.getLogger("tensorflow")


_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT, None))
_handler.addFilter(logging.Filter("tensorflow.monitor"))


_logger.addHandler(_handler)
_logger.setLevel(logging.INFO)

_logger.info('VOWF F DS F ')


_logger_monitor = logging.getLogger("tensorflow.monitor")
_logger_monitor.info('child logger message')

# 
# # logging.info('is when this event was logged.')
# logger.info('another logger')
# logger.warning('more     another logger')