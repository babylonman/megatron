# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:34:30 2018

@author: pi
"""

import serial
import pandas as pd


def get_position(serial_port, data_container):
# port is a serial object for GPS
# read data
# format into df
# return data frame
    print('called')
    d = {}
    readComplete = False
    while readComplete == False:
        line = str(serial_port.readline())
        [msg, data] = line[2:].split(',', 1)
#       for debug
        print('Received ' + msg)
        if msg == '$GPGLL':
# store into local variables
            [gps_lat, gps_latDir, gps_lon, gps_lonDir, gps_time,
             gps_valid, gps_cksum] = data.split(',', 6)
            for i in ('gps_lat', 'gps_latDir', 'gps_lon', 'gps_lonDir',
                      'gps_time', 'gps_valid'):
# fill dict d with keys for data fields and cooresponding data
                d[i] = locals()[i]
                dd = pd.DataFrame([d], columns=d.keys())
            print(dd)
            return store(dd, data_container)
            break


def store(data_dict, main_df):
    ''' Store data in larger dataframe during collection, can be dictionary'''
    for i in data_dict.keys():
        if i not in list(main_df):
            print('Data  key "' + i + '" is not in main dataframe')
            return main_df

    main_df = main_df.append(data_dict)

    return main_df


columns = ['gps_lat', 'gps_latDir', 'gps_lon', 'gps_lonDir', 'gps_time',
           'gps_valid']


df = pd.DataFrame(columns=columns)
ser = serial.Serial('/dev/ttyACM0')
df = get_position(ser, df)

for i in range(1):
    get_position(ser, df)

df = get_position(ser, df)
print(df)

r = {'check': 99, 'gps_valid': 'B'}
store(r, df)