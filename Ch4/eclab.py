from GF2 import *

def dot(v, w):
	return sum([ v[i] * w[i] for i, val in enumerate(v) ])

def mvmult(A, v):
	return [ dot(row, v) for row in A ]

# Check Matrix - H

# Generator Matrix - G
G = [
	[one, 0, one, one],
	[one, one, 0, one],
	[0, 0, 0, one],
	[one, one, one, 0],
	[0, 0, one, 0],
	[0, one, 0, 0],
	[one, 0, 0, 0]
]

# 4 bit message - p
p = [one, 0, 0, one]

print(mvmult(G, p))
