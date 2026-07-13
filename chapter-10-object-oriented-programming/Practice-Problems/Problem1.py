# Q1. Creat a class "Programmer" for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

e1 = Programmer("Yash", 1200000, 444802)
print(e1.name, e1.salary, e1.pin, e1.company)

e2 = Programmer("Anshu", 1300000, 444607)
print(e2.name, e2.salary, e2.pin, e2.company)