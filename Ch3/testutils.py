import utils as ut

if __name__ == '__main__':
	vecs = [[0, 0, 0], [1, 1, 1], [0, -1, 2.0]]

	print(ut.vadd(vecs[0], vecs[1])) # [1, 1,  1]
	print(ut.vadd(vecs[0], vecs[2])) # [0, -1, 2.0]
	print(ut.vadd(vecs[2], vecs[1])) # [1, 0,  3.0]
	print(ut.vadd(vecs[1], vecs[2])) # [1, 0,  3.0]



