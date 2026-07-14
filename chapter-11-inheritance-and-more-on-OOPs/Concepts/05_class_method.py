class Employee:
    a = 1
    @classmethod    # which give preferrence over instance attribute
    def show(cls):
        print(f"The class attronite of a is: {cls.a}")

e = Employee()
e.a = 45

e.show()