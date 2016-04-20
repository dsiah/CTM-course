from functools import reduce
from tools import *

# 1
def islinind(x):
	if type(x) is not list:
		print("Error: argument must be a list of vectors")
		return
	elif type(x[0]) is not list:
		print("Error: islinind needs to be supplied a list of vectors")
		return

	mat = rref(x)
	# RREF'd matrix will be identity matrix if linind & square
	if (shape(mat)[0] != shape(mat)[1]):
		dim = shape(mat)[0]
		id_mat = ID(dim)
		for row in range(dim):
			for col in range(dim):
				if mat[row][col] != id_mat[row][col]:
					return False
		return True
	else:
		# 
		rdim, cdim = shape(mat)[0], shape(mat)[1]
		zeror = 0
		for row in range(rdim):
			if _zero_row_check(mat[row]):
				zeror += 1
		# If the difference between rows and columns is greater
		# Than the zero rows after rref then not linear independent
		if abs(rdim - cdim) >= zeror:
			return False
		return True


def _zero_row_check(row):
	for r in range(len(row)):
		if row[r] != 0:
			return False
	return True

# 2
def isextra(i, x):
	
	if type(x) is not list:
		print("Error: second argument must be a list of vectors")
		return
	elif type(x[0]) is not list:
		print("Error: isextra needs to be supplied a list of vectors as second argument")
		return
	elif i >= len(x):
		print("Error: isextra cannot index, first arg cannot be bigger than length of second argument")
		return

	return islinind([r for r in x if r != i])

# 3
def coordinates(x, B):
	# inv(B) * B * coords = inv(B) * x
	# Figure out it RRE is possible on Mat B

	# Invert
	binv = reduceRowEchelon(B)
	# Multiply x by inverse of B
	return mmult(binv, transpose([x]))

# 4
def isUT(M):
	# Check square
	if type(M[0]) is not list:
		print("Error: input is not a matrix")
		return

	for row in range(len(M)):
		for col in range(len(M)):
			if row > col and M[row][col] != 0: 
				return False
	return True

# 5
def invertUT(M):
	# Check
	if not validUT(M):
		print("Error: input is not valid Upper Triangular Matrix")
		return

	dim = len(M)

	# Augment
	mat = augment(M, ID(dim))
	# Perform op's
	for i in range(dim):
		# Scale m[i][i] to 1
		if mat[i][i] != 1:
			mat = mmult(scale_row_mat(i, 1.0 / mat[i][i], dim), mat)

		# nullify the other nums in the column
		for j in [r for r in range(dim) if i != r]:
			mat = mmult(add_scaled_row_mat(i, -1* mat[j][i], j, dim), mat)
	
	return [row[dim:] for row in mat]

# 6 
def null(A):
	return rref(A)

# 7 
def Span(S):
	# S must have enough vectors to create the basis
	# If not vector set print error
	if type(x) is not list:
		print("Error: argument must be a list of vectors")
		return
	elif shape(S)[0] < shape(S)[1]:
		print("Error: not enough vectors in list to create basis")
		return

	basis = []
	# avoid 0 vector
	for v in S:
		basis.append(v)
		if not linind(basis):
			basis = basis[:len(basis) - 2]

	return basis

# 8
def backsub(A, b):
	# Assume uppertriangular, square, & non-singular
	ans = []

	for i in range(len(A) - 1, -1, -1):
		otre = sum([ a * o for a, o in zip(ans, A[i][i+1:])])
		ans.append((b[i] - otre) / A[i][i])

	return ans[::-1]

def _validUT(M):
	# Assume Square
	return sum([1 if M[i][i] != 0 else 0 for i in range(len(M))]) == len(M)


if __name__ == '__main__':
	mat = [[9, 0, 0], [0, 4, 1], [0, 0, 12]]
	ans = [2,3,4]
	# print(coordinates(ans, mat))
	# print(backsub(mat, ans))

	mat = [[1,1,1], [0,2,2], [0,0,3]]
	# ans = [5,6,-2]
	# print(backsub(mat, ans))

	invmat = invertUT(mat)
	# print(mmult(invmat, mat))

	mat2 = [[0,2,2], [1,1,1], [0,0,3]]
	invmat2 = reduceRowEchelon(mat2)


	mat3 = [[1,2,3], [2,1,1], [1,3,0]]
	invmat3 = reduceRowEchelon(mat3)

	# print(invmat3)
	# print(mmult(invmat3, mat3))

	mat4 = [[1,1,1,1], [1,2,3,4], [4,3,2,1]]

	mat5 = [[7,9], [6,10]]
	ab = coordinates([-2,2], mat5)
	# print(ab)
	print(mmult(mat5, ab))

	# print(rref(mat4))
