# -*- coding: utf-8 -*-
"""
Misc functions

Created on Sun Feb  4 09:48:50 2018

@author: pi
"""

import logging
import datetime as dt


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


def configure_logging(path='/home/pi/megatron/python/Log', filemode='w',
                      level=logging.DEBUG):
    '''Setup logging given a path and event serverity level

    Parameters
    ----------
    path = string
    path to log file directory

    level = logging event severity threshold

    Return
    ------
    n/a
    '''

    filename = 'Log_' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') \
               + '.log'
    print(filename)
    logging.basicConfig(filename=filename, level=level)
    logging.info('Begin')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
