# Q2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dogs' from 'Pets'. Add a method 'bark' to class 'Dogs'. 

class Animals:
    def __init__(self):
        print("This is Animal class")

class Pets(Animals):
    def __init__(self):
        print("This is Dogs class")

class Dogs(Pets):
    def __init__(self):
        print("This is Dogs class")

    @staticmethod
    def bark():
        print("Bow Bow!")

dogeshBhai = Dogs()
dogeshBhai.bark()