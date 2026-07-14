# Q7. Overrides the __len__() method on vector on problem 5 to display the dimensions of the vector.


class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))