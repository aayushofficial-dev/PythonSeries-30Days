# addition of two numbers

'''using + operators'''
a = 5
b = 7
res = a + b
print(res)

"""
Using sum() function
the sum() function adds all the values present in an iterable like a list or tuple and returns the total 
sum."""

nums = [10,5]
print(sum(nums))


"""
Using operator.add()
The operator module provides the add() function, which performs addition between two values similar 
to the + operator
"""
import operator
print(operator.add(10, 22))

"""
Using math.fsum()
The fsum() function from the math module is used for precise floating-point addition. It helps reduce
rounding errors while adding decimal values"""

import math
x = [0.01, 0.02]
print(math.fsum(x))

# Find the maximum of two numbers in Python

"""Using max()
max() function compares two or more values and returns the largest one. It performs the comparison internally
and eliminates the need to write explicit conditional statements."""

a = 7
b = 4
print(max(a, b))

"""Using Ternary operator
Ternary conditional operator evalutes the condition and return one of two values depending on whether 
the condition is true or false in a single expression"""

a = 7
b = 4

print(a if a > b else b)


"""
Using if-else statements
if-else statement evalutes a condition and executes one of two code blocks based on whether the condition is
true or false. It is used when the logic needs to be written explicitly in separate steps."""

a = 8
b = 7

if a > b:
    print(a)
else:
    print(b)

"""Factorial of a number in python"""

"""using math.factorial()
This method computes the factorial using Python's built-in factorial() function, which performs the
entire calculation internally without requiring loops or recursion in user code."""
import math 
n = 5
print(math.factorial(n))


"""Using NumPy's np.prod()
NumPy performs multiplication through optimized C-level operations. It computes the factorial by multiplying
all numbers from 1 to n in single vectorized step using np.road()"""
import numpy as np
n = 5
if n >= 0:
    print(np.prod(range(1, n + 1)))
else:
    print("Factorial is not defined for negative numbers.")

"""Using For Loop
This method calculates factorial by manually multiplying the numbers from 1 to n inside a for loop."""
n = 5 
if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)



"""Python program to find the largest element in an array.
example:
arr = [20, 10, 20, 30, 100]
output: 100"""

"""Using built-in max() function
Python has an inbuilt method max() which returns the maximum value among the arguements"""

arr = [10, 20, 30, 40, 50]
res = max(arr)
print(res)

"""Using Iteration
This method manually traverse the array and update the largest element when a bigger element is found."""

arr = [10, 324, 45, 90, 9808]
res = arr[0]

for i in range(1, len(arr)):
    if arr[i] > res:
        res = arr[i]
print(res)

"""Using reduce() Function
The reduce() function from functools can find the largest element by applying max cumulatively
across the array."""

from functools import reduce
arr = [10, 324, 45, 90, 9808]
res = reduce(max, arr)
print(res)

"""Using sort() function
Here sort() function is used to sort the array. The largest element will be the last element of the sorted array.
"""

arr = [10, 324, 45, 90, 9808]
arr.sort()
res = arr[-1]
print(res)

"""Using operator.gt()
Use the operator.gt() function to compare elements and find the largest element iteratively."""

import operator
arr = [1, 2, 3, 4, 5]
res = 0

for i in arr:
    if operator.gt(i, res):
        res = i
print(res)


"""Array rotation Without using slicing (using loops)"""

arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    first = arr[0]

    for j in range(len(arr) - 1):
        arr[j] = arr[j + 1]

    arr[-1] = first
print(arr) 

"""Right rotation"""
arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = arr[-1]

    for j in range(len(arr) - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)