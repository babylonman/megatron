# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:41:15 2018

@author: pi
"""

import logging
import logging.config
import datetime as dt

filename = dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') \
                + '_main.log'
logging.config.fileConfig('logging.conf', defaults={'logfilename': '../Log/'+filename})

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')