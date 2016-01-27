# David Siah -- Chapter 1 Tasks and Questions

import matplotlib.pyplot as plt
import image as img
from plotting import plot

S = set([2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 
         3+1j, 3.25+1j])

def plus_chart(s):
    for i in s:
        for j in s:
            print((i+j) % len(s), end=" ")
        print()

def mult_chart(s):
    for i in s:
        for j in s:
            print((i*j) % len(s), end=" ")
        print()


for i in range(2, 8):
    b = i - 2
    print("\n" + "="*b + " + " + "="*b)
    plus_chart({x for x in range(i)})
    print("\n" + "="*b + " * " + "="*b)
    mult_chart({x for x in range(i)})


def myplot(numset):
    X = [x.real for x in numset]
    Y = [x.imag for x in numset]
    plt.scatter(X,Y, color='red')
    plt.show()



face       = img.file2image('img01.png')
height     = len(face)
width      = len(face[0])

complixels = [(width - x) + (height - y) * 1j for y, row in enumerate(face) 
              for x, tup in enumerate(row) if tup[0] < (127.5)]
rot90 = [num * 1j for num in complixels]
center = [num - (width / 2) - ((height / 2) * 1j) for num in complixels]

# myplot(complixels)
# myplot(rot90)
# myplot(center)        
plot(complixels)
print(face[98][45])

# 1.7.1
def my_filter(L, num): return [x for x in L if x % num != 0]

# 1.7.2
def my_lists(L): return [range(i) for i in L]

# 1.7.3
def my_function_composition(f, g): {key: g[key] for key in F}

# 1.7.4
def mySum(L):
    curr = 0
    for i in L:
        curr += i
    return curr

# 1.7.5 Note: see https://en.wikipedia.org/wiki/Empty_product [] => 1
def myProduct(L):
    curr = 1
    for i in L:
        curr *= i
    return curr

# 1.7.6
def myMin(L):
    mini = None
    for i in L:
        if mini is None or i < mini:
            mini = i
    return mini

# 1.7.7
def myConcat(L):
    result = ''
    for i in L:
        result += i
    return result

# 1.7.8
def myUnion(L):
    curr = set()
    for s in L:
        curr = curr.union(s)
    return curr

# 1.7.9
# 1) Sum of empty set 0
# 2) Product of empty set is 1
# 3) None, or error in Python implementation
# 4) Concat of empty list of strings is ''
# 5) Union of empty list of sets is an empty set