-# -*- coding: UTF-8 -*-
from math import sqrt

# --------------- Presentation : ---------------------
# Thomas Ehling 08/24/18
# Sample code for python, including all the basics types and operations


# ------------------------- example of simple function  -------

# Squares
def quickSquare(arr):
    return [x ** 2 for x in arr]

print quickSquare([0, 1, 2, 3, 4])


# Sort an array
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print quicksort([1, 3, 6, 8, 4, 5, 2, 1, 9, 12])

# ------------------------- types  -------

# Integer
int_x = 3
print ((int_x + 1) * 2) ** 3

# Float
float_x = 2.5
print ((float_x + 1) * 2) ** 3

# Booleans
t, f = True, False
print (not ((t and f or t) == t))

# Strings
hello = 'hello'
print ('%s - %s - %d' % (hello, hello + " !", 77)).rjust(7).capitalize().replace('l', 'p').strip()

# List
list_x = [3, 12, 14, 48, 'hooora', 'hey']
print list_x[0]
print list_x[-1]
print list_x.append('olé')
print list_x.pop(), list_x

# Slicing (concize synthax to access sublists)
nums = range(5)
print nums
nums[2:4] = [8, 9]
print nums
print nums[2:4]
print nums[2:]
print nums[:2]
print nums[:]

# Dictionary : list with unics keys and associated values
dict_x = {'cats': 'cute', 'dogs': 'fury', 'elephants': 'awesome'}
print dict_x['elephants']
dict_x['unicorns'] = 'a miracle'
print dict_x
del dict_x['dogs']
print dict_x.get('dogs', 'Not found ;(')
print dict_x.get('unicorns', 'Not found ;(')
for animals in dict_x: print 'The %s are %s' % (animals, dict_x[animals])

# Sets : list with aan unordered collection of DISTINCTS elements
set_x = {'hot-dog', 'burger'}
print 'hot-dog' in set_x
print 'couscous' in set_x
print len(set_x)
set_x.add('hot-dog')
print len(set_x)
set_x.remove('hot-dog')
print len(set_x)
print {int(sqrt(x)) for x in range(37)}

# Tuples : Immutable list of value
t = (5, 6)
print t


