# Us
import routines as rt

# Them
import numpy as np

if __name__ == '__main__':
    # unittest.main()
    vec_a, vec_b = range(5), range(5)
    npa, npb = np.matrix(vec_a), np.matrix(vec_b)

    vec_c = [[1,2,3], [4,5,6], [7,8,9]]
    vec_d = [[0,1,0], [1,0,0], [1,0,1]]

    vec_e, vec_f = [[1,2,3], [4,5,6]], [[7,8], [9,10], [11, 12]]
    npc, npd = np.matrix(vec_c), np.matrix(vec_d)

    # Test vadd
    print(rt.vadd(vec_a, vec_b), npa + npb)

    # Test cmult
    print(rt.cmult(5, vec_a), npa * 5)

    # Test vzero
    print([0, 0, 0, 0, 0] == rt.vzero(5))
    print([] == rt.vzero(-1))

    # Test vneg
    print([-1,-2,-3] == rt.vneg(range(1,4)))

    # Test dot
    print(rt.dot(range(1,4), range(1,4)))

    print(rt.sbasis(4, 6))

    print(rt.vsum([vec_a, vec_b]), npa + npb)

    # Come back to this one
    print(rt.lincomb([1,2], [vec_a,vec_b]))

    print(rt.madd(vec_c, vec_d))

    print(rt.cmmult(5, vec_d))

    print(rt.mzero(5, 5))
    print(rt.mzero(3, 2))

    print(rt.mneg(vec_c))

    print(rt.ID(3))

    # print(rt.shape(vec_a))
    print(rt.shape(vec_c))
    print(rt.shape(rt.mzero(3, 2)))

    print(rt.transpose(vec_c))

    print(rt.mvmult(vec_c, range(1,4)))

    print(rt.mmult(vec_c, vec_d))
    print('TEST')
    print(npc * npd)

    print(rt.mmult(vec_e, vec_f))

    print(rt.acompatible(rt.ID(2), vec_c))
    print(rt.acompatible(rt.ID(3), vec_c))

    print(rt.mcompatible(rt.ID(2), vec_c))
    print(rt.mcompatible(rt.ID(3), vec_c))

    print(rt.mtov(vec_c))

    print(rt.swap(1, 2, vec_c))

    print(rt.addrow(2, 1, 2, vec_d))
    # Test augment
    print(rt.augment([[1,2,3], [4,5,6]], [[7],[8]]))

