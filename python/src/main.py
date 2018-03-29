# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:34:30 2018

@author: pi
"""

#import serial
import logging
import logging.config
import pandas as pd
import datetime as dt

import GPS_VK172 as vk
import path_plan as pp
import misc
import setup


# global setup
cal_file = 'cal_default.txt'


# setup logging
filename = dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') + '_main.log'
logging.config.fileConfig('logging.conf',
                          defaults={'logfilename': '../Log/'+filename})
logger = logging.getLogger('main')
logger.info('Begin log ' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p'))
misc.log_version()
cal = setup.cal_load(filename='calibration/'+str(cal_file))



df = vk.get_position()

rr = pp.load_waypoints()

for i in range(2):
    df = vk.get_position()
    logger.warning('position aquired.')

print(df)
logger.warning('hello')

r = {'check': 99, 'gps_valid': 'B'}
