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
	if len(clist) == 0 or len(vlist) == 0: return 0
	return reduce(vadd, [ cmult(clist[i], vlist[i]) for i, v in enumerate(vlist) ])

def madd(A, B):
	return [ vadd(arow, brow) for arow, brow in zip(A, B)]

def cmmult(c, A):
	return [ cmult(c, row) for row in A ]

def ID(n):
	return [ [ 1 if (row == col) else 0 for col in range(n) ] for row in range(n) ]

# Compliant with vector? No
def shape(A):
	return [ len(A), len(A[0]) ] # [rows, cols]

def transpose(A):
	return [ [ A[col][row] for col in range(len(A)) ] for row in range(len(A[0])) ]

def mmult(A, B):
	return [ [ dot(arow, brow) for brow in transpose(B)] for arow in A ]


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

def swap_row_mat(i, j, dim):
	iden = ID(dim)
	iden[i], iden[j] = iden[j], iden[i]
	return iden

def scale_row_mat(i, a, dim):
	iden = ID(dim)
	iden[i][i] = a
	return iden

def add_scaled_row_mat(org, a, tar, dim):
	iden = ID(dim)
	iden[tar][org] = a
	return iden

def validUT(M):
	# Assume Square
	return sum([1 if M[i][i] != 0 else 0 for i in range(len(M))]) == len(M)

def reduceRowEchelon(M):


	# Calculate size of Identity & Create
	dim = len(M)
	
	# Augment A with Identity
	mat = augment(M, ID(dim))

	# Work through elementary row operations
	for i in range(dim):
		# Find biggest in column and swap
		ind = findMaxIndex(M, i)
		if ind != i:
			mat = mmult(swap_row_mat(ind, i, dim), mat)

		# Scale m[i][i] to 1
		if mat[i][i] != 1 and mat[i][i] != 0:
			mat = mmult(scale_row_mat(i, 1.0 / mat[i][i], dim), mat)

		# nullify the other nums in the column
		for j in [r for r in range(dim) if i != r]:
			mat = mmult(add_scaled_row_mat(i, -1* mat[j][i], j, dim), mat)
	
	# Rip apart and return inverse A
	return [row[dim:] for row in mat]

def rref(M):

	# Calculate size of Identity & Create
	dim = len(M) # get num of rows
	mat = M[:]
	# Work through elementary row operations
	for i in range(dim):
		# Find biggest in column and swap
		ind = findMaxIndex(M, i)
		if ind != i:
			mat = mmult(swap_row_mat(ind, i, dim), mat)

		# Scale m[i][i] to 1
		if mat[i][i] != 1 and mat[i][i] != 0:
			mat = mmult(scale_row_mat(i, 1.0 / mat[i][i], dim), mat)

		# nullify the other nums in the column
		for j in [r for r in range(dim) if i != r]:
			mat = mmult(add_scaled_row_mat(i, -1* mat[j][i], j, dim), mat)

	return mat
	

	
def findMaxIndex(M, i):
	big = i
	for row in range(i+1, len(M)):
		if abs(M[row][i]) > abs(M[big][i]):
			big = row
	return big

def isSquare(M):
	return shape(M)[0] == shape(M)[1]

# Test
def isvectorset(x):
	return min([len(r) for r in x]) == max([len(r) for r in x])
# Test
def ismatrix(x):
	return shape(x)[0] == shape(x)[1]
