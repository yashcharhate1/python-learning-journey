class otherber:
    def __init__(self, n):
        self.n = n

    def __add__(self, other, num):
        return self.n + other.m + num.o
    
n = 1
m = 2
o = 3

print(n + m + o)