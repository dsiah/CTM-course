# 2 by 2
# Button Vectors (4)
tl = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 0}
tr = {(0, 0): 1, (0, 1): 1, (1, 0): 0, (1, 1): 1}
br = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
bl = {(0, 0): 1, (0, 1): 0, (1, 0): 1, (1, 1): 1}

def add_dict_gf2(d1, d2):
	return {key: (d1[key] + d2[key]) % 2 for key in d1.keys()}

print(add_dict_gf2(tl, tr))
print(add_dict_gf2(tl, bl))
print(add_dict_gf2(tl, br))

print(add_dict_gf2(tr, br))
print(add_dict_gf2(tr, bl))

print(add_dict_gf2(br, bl))
