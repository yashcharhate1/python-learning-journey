# Q5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [42, 7, 91, 15, 63, 28, 84, 3, 56, 19]

def max(a,b):
    if(a>b):
        return a
    return b

print(reduce(max, l))