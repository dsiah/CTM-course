from functools import reduce

def vadd(v, w):
	return [ (v[i] + w[i]) for i, val in enumerate(v) ]

def cmult(c, v):
	return [ (c * i) for i in v ]

def vzero(n):
	return [ 0 for i in range(n) ]

def vneg(v):
	return cmult(-1, v)

def dot(v, w):
	return sum([ v[i] * w[i] for i, val in enumerate(v) ])

# Treat indices the python way -- start from 0 go to n-1
# J is positive integer as specified so J=1 means index 0 or J - 1
def sbasis(j, n):
	return [ 1 if (i == j - 1) else 0 for i in range(n) ]

def vsum(vlist):
	return reduce(vadd, vlist)

def lincomb(clist, vlist):
	return reduce(vadd, [ cmult(clist[i], vlist[i]) for i, v in enumerate(vlist) ])

def madd(A, B):
	return [ vadd(arow, brow) for arow, brow in zip(A, B)]

def cmmult(c, A):
	return [ cmult(c, row) for row in A ]

def mzero(m, n):
	return [ [ 0 for col in range(n) ] for row in range(m) ]

def mneg(A):
	return [ [ (-1 * val) for val in row ] for row in A ]

def ID(n):
	return [ [ 1 if (row == col) else 0 for col in range(n) ] for row in range(n) ]

# Compliant with vector? No
def shape(A):
	return [ len(A), len(A[0]) ] # [rows, cols]

def transpose(A):
	return [ [ A[col][row] for col in range(len(A)) ] for row in range(len(A[0])) ]

def mvmult(A, v):
	return [ dot(row, v) for row in A ]

def mmult(A, B):
	return [ [ dot(arow, brow) for brow in transpose(B)] for arow in A ]

# Compliant with vector? No, must be matrix
def acompatible(A, B):
	return len(A) == len(B) and len(A[0]) == len(B[0])

# Compliant with vector? No, must be matrix
def mcompatible(A, B):
	return len(A) == len(B[0])

# Build list by reading off each row sequentially until final row
def mtov(A):
	mat = []
	for i in A:
		mat.extend(i)
	return mat

# J and K must index from 1
def swap(j, k, A):
	clone = [ row for row in A ]
	clone[j - 1], clone[k - 1] = clone[k - 1], clone[j - 1]
	return clone

# J and K must index from 1
def addrow(c, j, k, A):
	clone = [row for row in A]
	clone[k - 1] = vadd(clone[k - 1], cmult(c, clone[j - 1]))
	return clone

def augment(A, B):
	return [ arow + brow for arow, brow in zip(A, B)  ]

def invert(A):
	rows, cols = shape(A)
	if rows == cols:
		augie = augment(A, ID(rows))


if __name__ == '__main__':

	E_inv = [
		[[0, 1], [1, 0]],
		[[3, 0], [0, 1]],
		[[1, 0], [1, 1]],
		[[1, 0], [0, 2/3]],
		[[1, 4/3], [0, 1]],
		ID(2)
	]
	print(E_inv)
	print(mmult(reduce(mmult, E_inv[::-1]), [[1,2], [3, 4]]))

	print(mmult([[1,2], [3, 4]], reduce(mmult, E_inv[::-1])))
