# -*- coding: utf-8 -*-
"""
Functions for working with VK172 GPS device over serial interface

- add systime to dict
- add generic get_message('MSG') by name
- add logging

Created on Sat Feb  3 18:51:01 2018

@author: Jon Cosgrove
"""
import serial
import logging


def get_position(serial_port=None):
    '''Read GPS position, GPGLL, from VK-172

    Parameters
    ----------
    serial_port : serial.Serial object
    default = '/dev/ttyACM0'
    port of USB GPS receiver, Serial object from serial module

    Returns
    -------
    dict of position data, keys = format_GPGLL()

    Example
    -------
    current_positon = get_position(serial.Serial('/dev/ttyACM0'))
    '''

    if serial_port is None:
        try:
            default_port = '/dev/ttyACM0'
            serial_port = serial.Serial(default_port)
            logging.debug('Using default serial port %s', default_port)
        except:
            print('No serial port avaliable')
            logging.error('No serial port avaliable')
            return

    d = {}
    readComplete = False
    while readComplete == False:
        line = str(serial_port.readline())
        [msg, data] = line[2:].split(',', 1)
        # for debug
#        print('Received ' + msg)
        if msg == '$GPGLL':
            # store into local variables
            [gps_lat, gps_latDir, gps_lon, gps_lonDir, gps_time,
             gps_valid, gps_cksum] = data.split(',', 6)
            logging.debug('Message GPGLL received')
            for i in format_GPGLL():
                # fill dict d with keys for data fields and cooresponding data
                d[i] = locals()[i]
            return d


def format_GPGLL():
    '''Return a list of strings, format from GPGLL read'''

    return ['gps_lat', 'gps_latDir', 'gps_lon', 'gps_lonDir',
            'gps_time', 'gps_valid']
