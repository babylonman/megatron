
#~ https://codereview.stackexchange.com/questions/86421/line-segment-to-circle-collision-algorithm

from __future__ import division
import numpy as np
import math


#~ Q = np.array([2, 4]) # Centre of circle
#~ r = np.array([3])                # Radius of circle
#~ P1 = np.array([1, 7])     # Start of line segment
#~ V = np.array([10, 7]) - P1  # Vector along line segment
#~ print('\n' + 'This case should show one tangent intersection')

#~ Q = np.array([3, 9]) # Centre of circle
#~ r = np.array([1])                # Radius of circle
#~ P1 = np.array([1, 7])     # Start of line segment
#~ V = np.array([10, 7]) - P1  # Vector along line segment
#~ print('\n' + 'This case should not show an intersections')

Q = np.array([6, 6]) # Centre of circle
r = np.array([2])                # Radius of circle
P1 = np.array([1, 7])     # Start of line segment
V = np.array([10, 7]) - P1  # Vector along line segment
print('\n' + 'This case should show two intersections')

def line_cir_int():

	print('\n')
	print('Center of circle: 		' + str(Q))
	print('Radius of circle: 		' + str(r))
	print('Start of line: 			' + str(P1))
	print('Vector along line segment: 	' + str(V))
	print('\n')

	a = np.dot(V,V)
	b = 2 * np.dot(V, (P1 - Q))
	c = np.dot(P1,P1) + np.dot(Q,Q) - 2 * np.dot(P1,Q) - r**2

	disc = b**2 - 4 * a * c
	if disc < 0:
		print('descriminant is negative! no solutions \n')
		return False, None
		
	sqrt_disc = math.sqrt(disc)
	t1 = (-b + sqrt_disc) / (2 * a)
	t2 = (-b - sqrt_disc) / (2 * a)
	
	print('t1 : ' + str(t1))
	point1 = P1 + t1 * V
	print('Point 1 : ' + str(point1))
	print('t2 : ' + str(t2))
	point2 = P1 + t2 * V
	print('Point 2 : ' + str(point2))

	if not (0 <= t1 <= 1 or 0 <= t2 <= 1):
		return False, None
		
	t = max(0, min(1, - b / (2 * a)))
	
	print('P1 = ' + str(P1))
	print('t = ' + str(t))
	print('V = ' + str(V))
	
	return True, P1 + t * V

r = line_cir_int()
print(r)
