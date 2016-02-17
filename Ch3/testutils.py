import utils as ut

if __name__ == '__main__':
	vecs = [[0, 0, 0], [1, 1, 1], [0, -1, 2.0]]

	print(ut.vadd(vecs[0], vecs[1])) # [1, 1,  1]
	print(ut.vadd(vecs[0], vecs[2])) # [0, -1, 2.0]
	print(ut.vadd(vecs[2], vecs[1])) # [1, 0,  3.0]
	print(ut.vadd(vecs[1], vecs[2])) # [1, 0,  3.0]

	print(ut.smult(10, vecs[1]))

	print(ut.vzero(10))

	print(ut.vneg(vecs[1])) # [-1, -1, -1]
	print(ut.vneg(vecs[2])) # [0, 1, -2.0]

	print(ut.dot(vecs[1], vecs[2])) # 1
	
	print(ut.sbasis(-1, 5))	# [0, 0, 0, 0, 0]
	print(ut.sbasis(2, 5))  # [0, 1, 0, 0, 0]

	print(ut.vsum(vecs))    # [1, 0, 3.0]



