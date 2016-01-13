# 0.5.1
print(1 * 60 * 24 * 7)

# 0.5.2
print(2304811, '-', (2304811 // 47) * 47, '=', 2304811 - (2304811 // 47) * 47)

# 0.5.3
print('(673 + 909) % 3 == 0', (673 + 909) % 3  == 0)

# 0.5.4
x, y = -9, 1/2
print(2**(y + 1/2) if x + 10 < 0 else 2**(y - 1/2))

# 0.5.5
print({i**2 for i in {1,2,3,4,5}})

# 0.5.6
print({2**i for i in {0,1,2,3,4}})

# 0.5.7
print({x*y for x in {1,2,3} for y in {5,6,7}})

# 0.5.8
print({x*y for x in {0,2,3} for y in {4,6,9} if x != y})

# 0.5.9
print({x for x in {1,2,3,4} for y in {3,4,5,6} if x == y})

# 0.5.10
l = [20, 10, 15, 17]
print(sum(l) / len(l))

# 0.5.11
print([[a, b] for a in ['A', 'B', 'C'] for b in [1, 2, 3]])

# 0.5.12
LofL = [[1,2,3], [0.6, 0.8], range(100)]
print(sum([sum(i) for i in LofL]))

# 0.5.13
# [a,b,c] = [1,2] # Error!
# print(a,b,c)

# 0.5.14
s = {-4,-2,1,2,5,0}
print([(i, j, k) for i in s for j in s for k in s if sum([i,j,k]) == 0])

#  0.5.15
print([(i, j, k) for i in s for j in s for k in s if sum([i,j,k]) == 0 
			 and i != k and k != j and i != j])

# 0.5.16
print([(i, j, k) for i in s for j in s for k in s if sum([i,j,k]) == 0 
				and i != k and k != j and i != j][0])

# 0.5.17
L = [1, 1, 2, 3]
print(len(L), len(list(set(L))))

# 0.5.18
print({i for i in range(100) if i % 2 != 0})

# 0.5.19
print(list(zip(range(5), ['A', 'B', 'C', 'D', 'E'])))

# 0.5.20
print([sum(i) for i in zip([10, 25, 40], [1, 15, 20])])

# 0.5.21
dlist = [{'James': 'Sean',   'director': 'Terence'}, 
				 {'James': 'Roger',  'director': 'Lewis'}, 
				 {'James': 'Pierce', 'director': 'Roger'}]
k = 'James'
print([i[k] for i in dlist])

# 0.5.22
dlist = [{'Bilbo': 'Ian',    'Frodo':  'Elijah'},
				 {'Bilbo': 'Martin', 'Thorin': 'Richard'}]
k = 'Frodo'
print([i[k] if k in i else 'NOT PRESENT' for i in dlist])

# 0.5.23
print({k:k**2 for k in range(100)})

# 0.5.24
D = {'red', 'white', 'blue'}
print({i:i for i in D})

# 0.5.25
base = 10
# digits = set(range(base))
print({(a * base**2 + b * base**1 + c * base**0):[a,b,c] 
			 for a in range(base) for b in range(base) for c in range(base)})

# 0.5.26
id2salary = {0:1000.0, 3:990, 1:1200.50}
names = ['Larry', 'Curly', '', 'Moe']
print({ names[i]:val for (i, val) in id2salary.items() })

# 0.5.27
def twice(z): return 2*z
z = 10
print(twice(z))
z = 'Hello'
print(twice(z))

# 0.5.28
def nextInts(L): return [i + 1 for i in L]
print(nextInts([1,2,3]))

# 0.5.29
def cubes(L): return [i ** 3 for i in L]
print(cubes([1,2,3]))

# 0.5.30
def dict2List(dct, keylist): return [dct[i] for i in keylist]
print(dict2List({'a': 'A', 'b': 'B', 'c': 'C'}, ['b', 'c', 'a']))

# 0.5.31
def list2Dict(L, keylist): return {i:j for (i, j) in zip(keylist, L)}
print(list2Dict(['A', 'B', 'C'], ['a', 'b', 'c']))

# 0.5.32
def all_3_digit_numbers(base, digits): 
	return {(a * base**2 + b * base**1 + c * base**0)
					for a in range(base) for b in range(base) for c in range(base)}
print(all_3_digit_numbers(3, range(3)))

# 0.6.1
# help(math)
import math

# 0.6.2
from random import randint
def movie_review(name): 
	return ['See it!', 'A gem', 'Ideological claptrap rivaling Ayn Rand'][randint(0,2)]

# 0.6.3
# See dictutil.py

# 0.6.4
def listrange2Dict(L): return {i:j for (i, j) in zip(range(len(L)), L)}

for i in [1,2,3]:
	y = i * i
	print(y)