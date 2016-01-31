import math

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


# 2.3.6
a = { (a,b): (a * 200 + b * 20) / 1100 for a in range(6) for b in range(6) }

# 2.6.9
def segment(pt1, pt2):
	'''
	(TODO)
	Get 100 evenly spaced points between pt1, and pt2 
	where pt1 and pt2 are the endpoints 
		pt1: [x y]
		pt2: [x y]
	'''
	pass