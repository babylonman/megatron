# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:12:48 2018

@author: pi
"""

import geojson as geo
import logging
import os
import numpy as np

from src import cubic_spline_planner as csp


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
    waypoints = load_waypoints('geojson/data/Baseball_feat_coll_dump.json')
    '''
#os.path.dirname(os.getcwd()) +
    if waypoint_file is None:
        waypoint_file = ('src/geojson/data/Baseball_feat_coll_dump.json')
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
    >>> import os
    >>> p = os.path.dirname(os.getcwd())
    >>> waypoint_file = 'geojson/data/Baseball_feat_coll_dump.json'
    >>> waypoints = geo.load(open(waypoint_file, 'r'))
    >>> next_waypoint(waypoints, 1).geometry.id
    2
    >>> next_waypoint(waypoints, -3)
    -1
    >>> del waypoint_file, waypoints
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


def plan_path(feature_collection, ds=None, closed_course=False):
    '''plan path

    Parameters
    -------
    feature_collection : geojson feature collection object
    ds = sample spacing for spline calculations [m]
    closed_course = False, course ends at last coordinate pair


    Returns
    -------
    sp : spline2D object

    Example
    -------

    Tests
    -----
    '''
    
    from src import location
    [x, y] = location.get_coord(feature_collection)

    if ds is None:
        dx = np.mean(np.diff(x))
        dy = np.mean(np.diff(y))
        ds = np.mean([dx, dy])/10

    sp = csp.calc_spline_course(x=x, y=y, ds=ds, view_plot=False,
                                closed_course=closed_course)
    return sp, x, y


waypoints = load_waypoints()
[sp, x, y] = plan_path(waypoints, closed_course=True)
csp.plot_spline_course(x, y, sp,)

# doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
