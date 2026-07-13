# Q2. Write a class "Calculator" capable fo finding square, cube and squre root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of number is {self.n ** 2}")
    
    def cube(self):
        print(f"The cube of number is {self.n ** 3}")
    
    def squareroot(self):
        print(f"The square root of number is {self.n ** 1/2}")
    
c = Calculator(4)
c.square()
c.cube()
c.squareroot()