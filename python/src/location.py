#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:24:30 2018

@author: joncosgrove
"""


import utm


def dd2utm(x=None, y=None, xy=None):
    ''' converts from decimal degrees to utm coordinates

    Parameters
    ----------
    x : single or list of coordinates in decimal degrees
    y : single or list of coordinates in decimal degrees

    Return
    ------
    If x and y are a single coordinate pair, return single utm coordinate pair
    If x and y are lists of coordinate pairs,
        return lists of utm coordinate pair in the same order

    Tests
    -----
    >>> [x1, y1] = get_coord(waypoints)
    >>> xy = list(zip(x1[0:2], y1[0:2]))
    >>> [x2, y2] = 34, -122
    >>> [x3, y3] = 34.21, -122.21

    List input example
    >>> dd2utm(xy=xy)
    [(584820.5827249154, 4137236.183529727, 10, 'S'), (584814.6156535968, 4137216.02884254, 10, 'S')]

    Single coordinate pair example
    >>> dd2utm(x2, y2)
    (592349.6033428713, 3762606.6599021987, 10, 'S')

    '''

    if xy:
        c = [utm.conversion.from_latlon(i[0], i[1]) for i in xy]
    else:
        c = utm.conversion.from_latlon(x, y)

    return c


def get_coord(feature_collection):
    ''' get x y coordinate pairs from geojson feature collection object
    Parameters
    ----------
    feature_collection : geojson feature collection object

    Tests
    -----
    >>> import geojson
    >>> import os
    >>> p = os.path.dirname(os.getcwd())
    >>> waypoint_file = p + '/test/path_plan/data/Baseball_feat_coll_dump.json'
    >>> waypoints = geo.load(open(waypoint_file, 'r'))
    >>> get_coord(waypoints)
    ([37.3779926, 37.3778115, 37.3777806, 37.3779436], [-122.0419519, -122.0420216, -122.0417949, -122.0417266])

    Return
    ------
    [x, y] list which preserves order found in feature_collection
    '''
    x, y = [], []
    for i in feature_collection.features:
        x.append(i.geometry.coordinates[0])
        y.append(i.geometry.coordinates[1])

    return x, y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
