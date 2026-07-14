# Q4. Write a class 'Complex' to represent the complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)    # o/p: <__main__.Complex object at 0x000001945CEFCB90>
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)    # o/p: 
    
    def __str__(self):
        return f"{self.r} + {self.i}i"  # o/p: 4 + 6i
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("Complex Addition")
print(c1 + c2)
print("Complex Multiplicaition")
print(c1 * c2)
