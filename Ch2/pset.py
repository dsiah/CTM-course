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


def dot_product_lists(v, w):
	return sum([x * y for (x, y) in zip(v, w)])

def dot_product_dicts(v, w):
	return sum([v.get(key, 0) * w.get(key, 0) for key in v.keys()])

# 2.9.1
b, c = [1, 1, 1, 1, 1], [10, 0, 20, 40, -100]
print(dot_product_lists(b, c))

# 2.9.7
D = {'radio', 'sensor', 'memory', 'CPU'}
rate = {'radio': 0.06, 'sensor': 0.004, 'memory': 0.1, 'CPU': 0.0025}
duration = {'radio': 0.2, 'sensor': 0.5, 'memory': 1.0, 'CPU': 1.0}

print(dot_product_dicts(rate, duration))


# 2.9.15 - useful for previous problems (2.9.13 and 2.9.14)
def dot_prods(needle, haystack):
	s, h = len(needle), len(haystack)
	return [dot_product_lists(needle, haystack[i: i+s]) for i in range(h - s)]

# 2.9.13
haystack = [1, -1, 1, 1, 1, -1, 1, 1, 1]
needle   = [1, -1, 1, 1, -1, 1]
print(dot_prods(needle, haystack))

# 2.9.14
haystack = [1,2,3,4,5,6]
needle   = [1,2,3]
print(dot_prods(needle, haystack))