# Parent 1 Class
class Employee:
    company = "Vrkaa"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def show(self):
        print(f"The name of the Employee is {self.name} and thier salary is {self.salary}")

# Parent 2 Class
class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Out of all langauges, here is your language: {self.language}")


# Derived or Child Class
class Programmer(Employee, Coder):
    company = "Vrkaa E-Commerce"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {Coder.language}")


a = Employee("Yash", 1200000, "JavaSript")
b = Programmer("Anshu", 1200000, "Pyh")
c = Coder()

print(a.company, b.company)

a.show()
b.show()
b.printLanguage()

print("Before showLanguage")
b.showLanguage()
