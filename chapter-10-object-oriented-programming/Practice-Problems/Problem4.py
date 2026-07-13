# Q4. Add a static method to problem 2, to hello user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of number is {self.n ** 2}")
    
    def cube(self):
        print(f"The cube of number is {self.n ** 3}")
    
    def squareroot(self):
        print(f"The square root of number is {self.n ** 1/2}")

    @staticmethod
    def hello():
        print("Hell0!")
    
c = Calculator(4)
c.hello()
c.square()
c.cube()
c.squareroot()