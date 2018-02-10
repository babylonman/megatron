# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:51:08 2017

@author: pi
"""

# import geojson file which is a list of points
# define relationships between points (sequence type, etc.)

with open('/home/pi/megatron/python/geojson/my_point_for_import.json', 'r') as f:
    my_imported_point = geojson.load(f)
    
loc = {'coordinates':'1', 'type', 'sequence', 'description'}

loc['coordinates']
