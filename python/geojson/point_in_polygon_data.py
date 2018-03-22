#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:43:15 2018

@author: joncosgrove
"""


from matplotlib import pyplot as plt
import shapely.geometry

x = [1,2,5,5,2,1]
y = [0,2,2,5,5,0]

x1 = [3,4,4,3,3]
y1 = [3,3,4,4,3]

x2 = [2,2,3.5,2,3.5]
y2 = [1,2,3,3,3.5]

p1 = geojson.Feature(geometry=geojson.Point((2,1))).geometry
p1s = shapely.geometry.shape(p1)
p2 = geojson.Feature(geometry=geojson.Point((2,2))).geometry
p2s = shapely.geometry.shape(p2)
p3 = geojson.Feature(geometry=geojson.Point((3.5,3))).geometry
p3s = shapely.geometry.shape(p3)
p4 = geojson.Feature(geometry=geojson.Point((2,3))).geometry
p4s = shapely.geometry.shape(p4)
p5 = geojson.Feature(geometry=geojson.Point((3.5,3.5))).geometry
p5s = shapely.geometry.shape(p5)
polygon = geojson.Feature(geometry=geojson.Polygon([[(1, 0), (2, 2), (5, 2), (5, 5), (2, 5), (1, 0)], [(3, 3), (4, 3), (4, 4), (3, 4), (3, 3)]])).geometry
poly = shapely.geometry.shape(polygon)

#plt.scatter(x,y)
plt.plot(x,y,x1,y1)
plt.scatter(x2,y2)
axes = plt.gca()
axes.set_xlim([0,6])
axes.set_ylim([0,6])



def point_in_polygon(point, polygon):
    '''
    Parameters
    -------
    point : Point in GeoJSON format.
    polygon : Polygon in GeoJSON format.

    Returns
    ---------
    4 : boundary condition
    3 : invalid polygon
    2 : invalid point
    1 : point in polygon
    0 : point not in polygon

    Example
    -------
    >>> import geojson
    >>> import json
    >>> point_in_polygon(json.loads('{"coordinates":[0,1],"type":"Point"}'),
    ...     json.loads('{"coordinates":[[[0,1],[5,5],[10,0],[0,1]]],'
    ...         '"type":"Polygon"}'))
    4

    Tests
    -----
    >>> polygon = geojson.Feature(geometry=geojson.Polygon([[(1, 0), (2, 2), (5
    ...     , 2), (5, 5), (2, 5), (1, 0)], [(3, 3), (4, 3), (4, 4), (3, 4), (3,
    ...     3)]])).geometry

    1. point outside polygon exterior perimeter, return 0
    >>> point = geojson.Feature(geometry=geojson.Point((2, 1.9))).geometry
    >>> point_in_polygon(point, polygon)
    0
    
    2. point lies on segment, return 4
    >>> point = geojson.Feature(geometry=geojson.Point((3, 5))).geometry
    >>> point_in_polygon(point, polygon)
    4
    
    3. point lies on polygon vertex, return 4
    >>> point = geojson.Feature(geometry=geojson.Point((1, 0))).geometry
    >>> point_in_polygon(point, polygon)
    4
    
    4. point lies within polygon, return 1
    >>> point = geojson.Feature(geometry=geojson.Point((2.5, 2.5))).geometry
    >>> point_in_polygon(point, polygon)
    1
    
    5. point within exterior perimeter but not within polygon, within hole,
       return 0
    >>> point = geojson.Feature(geometry=geojson.Point((3.5, 3.5))).geometry
    >>> point_in_polygon(point, polygon)
    0
    
    6. invalid point, return 2
    >>> point_in_polygon(0, polygon)
    2
    
    7. invalid polygon, return 3
    >>> point_in_polygon(point, 0)
    3
    >>> polygon = geojson.Feature(geometry=geojson.Polygon(
    ...     [[(2, 2), (2, 5), (2, 2)]])).geometry
    >>> point_in_polygon(point, polygon)
    3
    '''
    # invalid point
    try:
        point = shapely.geometry.shape(point)
    except Exception:
        return 2
    if not point.is_valid:
        return 2
        
    # invalid polygon
    try:
        polygon = shapely.geometry.shape(polygon)
    except Exception:
        return 3
    if not polygon.is_valid:
        return 3
        
    # boundary conditions
    if point.touches(polygon):
        return 4
    
    # point not in polygon
    if not point.intersects(polygon):
        return 0
        
    # point in polygon
    return 1

print(point_in_polygon(p1s,poly))
print(point_in_polygon(p2s,poly))
print(point_in_polygon(p3s,poly))
print(point_in_polygon(p4s,poly))
print(point_in_polygon(p5s,poly))


if __name__ == "__main__":
    import doctest
    doctest.testmod()