# Base Class
class Employee:
    company = "Vrkaa"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def show(self):
        print(f"The name of the Employee is {self.name} and thier salary is {self.salary}")

    # There can be multiple methods in Base Class


''' Instead of writing or Copy/Paste every method of Base Class Employee '''

# class Programmer:
#     company = "Vrkaa E-Commerce"
#
#     def show(self):
#         print(f"The name of the Employee is {self.name} and thier salary is {self.salary}")
#
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language}")


''' We use Inheritance '''
# Derived or Child Class
class Programmer(Employee):
    company = "Vrkaa E-Commerce"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")    # New Attribute/Method


a = Employee("Yash", 1200000, "Python")
b = Programmer("Anshu", 1200000, "Python")

print(a.company, b.company)
a.show()
b.show()
print("Before showLanguage")
b.showLanguage()
