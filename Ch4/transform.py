# Use matrix-vector multiplication to geometrically transform the point
# Ex.
# x, y = 12, 15
# pt   = [x, y]
# tm   = [[1, 0], [0, 2]]
from math import sin, cos, pi
import image_mat_util as imu 

def identity():
	return [[1 if (row == col) else 0 for col in range(3)] for row in range(3)]

def translation(alpha, beta):
	mat = identity()
	mat[0][-1] = alpha
	mat[1][-1] = beta
	return mat 

def scale(alpha, beta):
	mat = identity()
	mat[0][0] = alpha
	mat[1][1] = beta
	return mat

def rotation(theta):
	mat = identity()
	mat[0][0] = cos(theta)
	mat[0][1] = -sin(theta)
	mat[1][0] = sin(theta)
	mat[1][1] = cos(theta)
	return mat

def rotation_about(theta, x, y):
	pass

def reflect_y():
	mat = identity()
	mat[0][0] = -1
	return mat

def scale_color(r, g, b):
	pass

def grayscale():
	pass

def reflect_about(x1, y1, x2, y2):
	pass