#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:50:59 2018

@author: joncosgrove

setup calibration file as a dict containing a parameter, value, and unit
example: cal['waypoint_tolerance'] = {'value': 2, 'unit': 'm'}

"""

import json


def cal_set():
    ''' sets parameter value temporarly for the given test run
    '''
    pass


def cal_get():
    ''' returns the current value of the parameter passed to the get call
    '''
    pass


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


def cal_load(filename='calibration/cal_default.txt'):
    ''' loads the given calibration file
    '''
    with open(filename, 'r') as file:
        cal = json.loads(file.read())
    return cal


def cal_example_setup():
    cal = {}
    cal['waypoint_tolerance'] = {'value': 2, 'unit': 'm'}
    cal['max_speed'] = {'value': 100, 'unit': 'rpm'}
    with open('calibration/cal_default.txt', 'w') as file:
        file.write(json.dumps(cal))
    return
