# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:34:30 2018

@author: pi
"""

#import serial
import logging
import logging.config
import pandas as pd
from Src import GPS_VK172 as vk
import datetime as dt


# setup logging
filename = dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') + '_main.log'
logging.config.fileConfig('Src/logging.conf',
                          defaults={'logfilename': 'Log/'+filename})
logger = logging.getLogger('main')
logger.info('Begin log ' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p'))

df = vk.get_position()

for i in range(10):
    df = vk.get_position()
    logger.warning('position aquired.')

print(df)
logger.warning('hello')

r = {'check': 99, 'gps_valid': 'B'}
