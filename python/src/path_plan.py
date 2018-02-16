# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:12:48 2018

@author: pi
"""

import geojson as geo
import logging
import os


def load_waypoints(waypoint_file=None):
    '''Loads waypoints from geojson dump file
    Parameters
    -------
    waypoint_file : string, default = None
        path to .json file containing feature collection

    Returns
    -------
    geojson feature collection object

    Example
    -------
    waypoints = load_waypoints(/home/pi/megatron/python/geojson/data/test.json
    '''

    if waypoint_file is None:
        waypoint_file = '/home/pi/megatron/python/geojson/data/Baseball_feat_coll_dump.json'
    with open(waypoint_file, 'r') as f:
        r = geo.load(f)
        logging.info('Using waypoint data from' + str(waypoint_file))
        return r


def next_waypoint(feature_collection=None, current_id=1):
    '''Finds the next waypoint in feature collection
    if current id is the last, returns the first, as in a loop

    Parameters
    -------
    feature_collection : geojson feature collection object
    current_id : number
        index of current feature geometry id, to be advanced

    Returns
    -------
    geojson feature object

    Example
    -------
    target = next_waypoint(waypoints, 2)

    Tests
    -----
    >>> import geojson
    >>> geo.load('/home/pi/megatron/python/Test/path_plan/data/Baseball_feat_coll_dump.json')
    >>> next_waypoint(waypoints, 1)
    >>> 2
    >>> next_waypoint(waypoints, -3)

    '''
    if current_id < 0:
        return -1

    for i in feature_collection.features:
        if i.geometry.id == current_id + 1:
            return i
            break
# need to track min and max geo id outside of this function for efficiency
# max to be referenced to determine when to loop back to first as well as
# out of range checks
    logging.warning('current_id out of range')
    return -1

waypoints = load_waypoints()

# test of next_waypoint
print('should return 2')
r = next_waypoint(waypoints, 1)
print(r.geometry.id)
print(r.geometry.coordinates)
