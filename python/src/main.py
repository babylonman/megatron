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
import location
import sm
import pure_pursuit

machine = sm.Machine()



filename = '../log/' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') + '_main.log'
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=filename, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('Begin log ' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p'))

machine.stop()


# global setup
cal_file = 'cal_test.txt'
misc.log_version()
cal = setup.cal_load()


location.start_gps()


df = vk.get_position()

rr = pp.load_waypoints()

pure_pursuit.main()

for i in range(2):
    df = vk.get_position()

print(df)

