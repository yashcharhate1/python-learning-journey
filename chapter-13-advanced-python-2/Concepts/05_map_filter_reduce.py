from functools import reduce

# Map Example

l = [1, 2, 3, 4, 5]

square = lambda x : x**2

sqList = map(square, l)
print(list(sqList))     # Output: [1, 4, 9, 16, 25]


# Filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))   # Output: [2, 4]


# Reduce Example
def sum(a,b):
    return a+b

mul = lambda x,y : x*y

print(reduce(sum, l))   # Output: 15
print(reduce(mul, l))   # Output: 120
