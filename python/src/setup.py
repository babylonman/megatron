#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:50:59 2018

@author: joncosgrove

setup calibration file as a dict containing a parameter, value, and unit
example: cal['waypoint_tolerance'] = {'value': 2, 'unit': 'm'}

"""

import json
import logging


def cal_set(parameter, value):
    ''' sets parameter value temporarly for the given test run
    '''
    try:
        cal
    except NameError:
        logger.warning('Calibration not loaded, cal_get() attempted')
    else:
        try:
            cal[parameter]['value'] = value
            return logger.info('Calibration parameter : ' +
                                str(parameter) + ' set to : ' + str(value) +
                                ' ' + str(cal[parameter]['unit']))
        except KeyError:
            return logger.warning('Parameter not defined in current calibration')


def cal_get(parameter):
    ''' returns the current value of the parameter passed to the get call
    '''
    global cal
    try:
        cal
    except NameError:
        logger.warning('Calibration not loaded, cal_get() attempted')
    try:
        return cal[parameter]['value']
    except KeyError:
        return logger.warning('Parameter not defined in current calibration')


def cal_save():
    ''' saves the current values of all parameters to a new calibration file
    using the name given
    '''
    pass


def cal_reset():
    ''' resets the current calibration values to defaults, or to the
    calibration file given
    '''
    pass


def cal_list():
    ''' lists the avaliable calibration parameters from the calibration file
    given
    '''
    pass


def cal_desc():
    ''' prints a description of the given calibration parameter
    '''
    pass


def cal_load(filename='calibration/cal_default.txt'):
    ''' loads the given calibration file
    '''
    with open(filename, 'r') as file:
        cal = json.loads(file.read())
    print('cal loaded')        
    logger.info('Calibration file loaded : ' + filename)
    return cal


def cal_example_setup():
    cal = {}
    cal['waypoint_tolerance'] = {'value': 2, 'unit': 'm'}
    cal['max_speed'] = {'value': 100, 'unit': 'rpm'}
    with open('calibration/cal_example.txt', 'w') as file:
        file.write(json.dumps(cal), sort_keys=True,
                   indent=4, separators=(',', ': '))
    return

logger = logging.getLogger(__name__)
cal = cal_load()