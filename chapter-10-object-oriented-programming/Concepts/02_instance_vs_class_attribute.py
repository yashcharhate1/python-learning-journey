class Employee:
    language = "Python"     # language is a class attribute
    salary = 1200000        

yash = Employee()       # Object instantiation
yash.language = "JavaScript"     # instance attribute # Instance attribute take preferrence over class attributes
print(yash.language, yash.salary)
