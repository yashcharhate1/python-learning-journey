class Employee:
    language = "Python"     # language is a class attribute
    salary = 1200000        # salary is a class attribute

yash = Employee()       # Object instantiation
yash.name = "Yash Charhate"     # instance attribute
print(yash.name, yash.language, yash.salary)

zoro = Employee()       # Object instantiation
zoro.name = "Roronoa Zoro Robinson"     # instance attribute
print(zoro.name, zoro.salary, zoro.language)


# Here ".name" is an instace/object attribute,
# whereas "language" and "salary" are class attributes as they directly 
# belong to the class