# Q1. Create a class (2-D Vector) and use it to create another class representing a 3-D Vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2-D vetor is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The 3-D vetor is {self.i}i + {self.j}j + {self.k}k")

obj1 = TwoDVector(1, 2)
obj1.show()

obj2 = ThreeDVector(5, 4, 3)
obj2.show()
