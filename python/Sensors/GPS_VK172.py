# -*- coding: utf-8 -*-
"""
Functions for working with VK172 GPS device over serial interface

Created on Sat Feb  3 18:51:01 2018

@author: Jon Cosgrove
"""


def get_position(serial_port):
    '''Read GPS position, GPGLL, from VK-172

    Parameters
    ----------
    serial_port : serial.Serial object
    port of USB GPS receiver, Serial object from serial module

    Returns
    -------
    dict of position data, keys = format_GPGLL()

    Example
    -------
    current_positon = get_position(serial.Serial('/dev/ttyACM0'))

    '''

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
            for i in format_GPGLL():
                # fill dict d with keys for data fields and cooresponding data
                d[i] = locals()[i]
            return d


def format_GPGLL():
    '''Return a list of strings, format from GPGLL read'''

    return ['gps_lat', 'gps_latDir', 'gps_lon', 'gps_lonDir',
            'gps_time', 'gps_valid']
