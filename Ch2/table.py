# Vector Addition [list]
def vadd_list(v, w): 
	return [ a + b for a, b in zip(v,w) ]

# Scalar Multiply [list]
def smult_list(a, v): 
	return [ i * a for i in v ]

# Vector Addition [dict]
def vadd_dict(v, w):
	return { key: v.get(key, 0) + w.get(key, 0) for key in v.keys() | w.keys() }

# Scalar Multiply [dict]
def smult_dict(a, v): 
	return { key: v[key] * a for key in v.keys() }

# Create Zero-vector [List] over Domain D 
def v_zero_list(D): 
	return [ 0 for i in D ]

# Create Zero-vector [Dict] over Domain D 
def v_zero_dict(D): 
	return { i: 0 for i in D }

def v_zeron_list(n): 
	return [ 0 for i in range(n) ]

def v_zeron_dict(n):
	return { i:0 for i in range(n) }

def equal_lists(v, w):
	'''
		Iterate through both vectors checking values
		returns true if they have same keys and values
	'''
	if len(v) != len(w):
		return False

	for i in range(min(len(v), len(w))):
		if v[i] != w[i]: return False

	return True

def equal_dicts(v, w):
	'''
		If union of both key sets is different then 
		keys of v are different than keys of w
	'''
	if (v.keys() | w.keys) != v.keys():
		return False  

	for key in v.keys():
		if v.get(key) != w.get(key):
			return False

	return True


def get_element_list(v, D, a):
	'''
		v: vector to get element from
		D: list with all possible domain values
		a: the key you are looking for
	'''
	if a not in D: raise KeyError

	return v[D.index(a)]



def get_element_dict(v, D, a):
	'''
		v: vector to get element from
		D: list with all possible domain values
		a: the key you are looking for

		Note: the get method will return 0
		for a value not contained in the dictionary (sparse)
	'''
	if a not in D: raise KeyError

	return v.get(a, 0)


def get_element_list(v, a):
	'''
		v: vector to get element from
		a: the key you are looking for, will be zero-index int
	'''
	return v[a]



def get_element_dict(v, a):
	'''
		v: vector to get element from
		a: the key you are looking for

		Note: the get method will return 0
		for a value not contained in the dictionary (sparse)
	'''
	return v.get(a, 0)

def set_element_list(v, k, a):
	if (k >= len(v) or k < 0):
		raise KeyError
	v[k] = a

def set_element_dict(v, k, a):
	v[k] = a

def set_element_dict(v, D, d, a):
	if d not in D:
		raise KeyError 

	v[d] = a

if __name__ == '__main__':
	# set_element_dict({}, [0, 1, 2, 3], 4,   1)
	# set_element_dict({}, [0, 1, 2, 3], '3', 1)
	a = {}
	set_element_dict(a, range(4), 3, 1)
	print(a)
