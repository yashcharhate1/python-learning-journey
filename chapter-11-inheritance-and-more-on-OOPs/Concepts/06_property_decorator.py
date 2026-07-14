class Employee:
    a = 1
    @classmethod    # which give preferrence over instance attribute
    def show(cls):
        print(f"The class attronite of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Yash Charhate"
print(e.fname, e.lname)

e.show()