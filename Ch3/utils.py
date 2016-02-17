class LengthError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def vadd(v, w):
    '''
        Vector addition (vectors must be same length)
            - v is the first vector 
            - w is the second vector

    '''
    if type(v) is not list or type(w) is not list:
    	raise TypeError('Input was not a lists')
    elif len(v) != len(w):
        raise LengthError('{} and {} must be equal in length'.format(v, w))

    return [i + j for (i, j) in zip(v, w)]

def smult(a, v):
    '''
        Scalar multiplation 
            - a is the scalar 
            - v is the vector
    '''

    return [i * a for i in v]

def vzero(n):
    '''
        Return an n-vector of 0s
    '''
    if type(n) is not int or n < 1:
    	raise TypeError('Input must be a positive integer')

    return [0 for i in range(n)]

def vneg(v):
	'''
		Return additive inverse of V 
			In this case, we are dealing with vectors over the Real numbers
			so, it is all the negative numbers
	'''
	if type(v) is not list:
		raise TypeError('Input was not a list')

	return [-1 * i for i in v]

def dot(v, w):
    '''
        Return the dot product of two vectors v & w
    '''
    if type(v) is not list or type(w) is not list:
    	raise TypeError('Input was not a lists')
    elif len(v) != len(w):
        raise LengthError('{} and {} must be equal in length'.format(v, w))

    return sum([i * j for (i, j) in zip(v, w)])
    
def sbasis(j, n):
    '''
        Create vector of length n with a 1 in the jth position
    '''
    return [1 if (i == j - 1) else 0 for i in range(n)]

def vsum(vlist):
    '''
        Sum all vectors into a single vector
    '''
    return reduce(vadd, vlist)
