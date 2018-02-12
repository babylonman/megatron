
#~ https://pypi.python.org/pypi/geojson/1.3.2

import geojson as geo




import geojson

my_point = geojson.Point((11.24, -1.532))

my_point  # doctest: +ELLIPSIS
{"coordinates": [43.2, -1.53], "type": "Point"}

dump = geojson.dumps(my_point, sort_keys=True)

dump  # doctest: +ELLIPSIS
'{"coordinates": [43.2, -1.53], "type": "Point"}'

geojson.loads(dump)  # doctest: +ELLIPSIS
{"coordinates": [43.2, -1.53], "type": "Point"}

# write to json file
geojson.dump(my_point, f)

# import from json file
with open('/home/pi/megatron/python/geojson/my_point_for_import.json', 'r') as f:
    my_imported_point = geojson.load(f)






from geojson import Point

Point((-115.81, 37.24))  # doctest: +ELLIPSIS
{"coordinates": [-115.8, 37.2], "type": "Point"}


from geojson import MultiPoint

MultiPoint([(-155.52, 19.61), (-156.22, 20.74), (-157.97, 21.46)])  # doctest: +ELLIPSIS
{"coordinates": [[-155.5, 19.6], [-156.2, 20.7], [-157.9, 21.4]], "type": "MultiPoint"}


from geojson import LineString

LineString([(8.919, 44.4074), (8.923, 44.4075)])  # doctest: +ELLIPSIS
{"coordinates": [[8.91, 44.407], [8.92, 44.407]], "type": "LineString"}


from geojson import MultiLineString

MultiLineString([
     [(3.75, 9.25), (-130.95, 1.52)],
     [(23.15, -34.25), (-1.35, -4.65), (3.45, 77.95)]
 ])  # doctest: +ELLIPSIS
{"coordinates": [[[3.7, 9.2], [-130.9, 1.52]], [[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]], "type": "MultiLineString"}


from geojson import Polygon

 # no hole within polygon
Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])  # doctest: +ELLIPSIS
{"coordinates": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "type": "Polygon"}

 # hole within polygon
Polygon([
     [(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)],
     [(-5.21, 23.51), (15.21, -10.81), (-20.51, 1.51), (-5.21, 23.51)]
 ])  # doctest: +ELLIPSIS
{"coordinates": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]], [[-5.2, 23.5], [15.2, -10.8], [-20.5, 1.5], [-5.2, 23.5]]], "type": "Polygon"}


from geojson import MultiPolygon

MultiPolygon([
     ([(3.78, 9.28), (-130.91, 1.52), (35.12, 72.234), (3.78, 9.28)],),
     ([(23.18, -34.29), (-1.31, -4.61), (3.41, 77.91), (23.18, -34.29)],)
 ])  # doctest: +ELLIPSIS
{"coordinates": [[[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}



