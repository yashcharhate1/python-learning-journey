class Employee:
    language = "Python"
    salary = 1200000   

    def getInfo(self):
        print(f"The languauge is {self.language}. And salary is {self.salary}")

    def greet(self):
        print("Good Morning!")

yash = Employee()
yash.language = "JavaScript"

yash.greet()
yash.getInfo()      # It is same as Employee.getInfo(yash)

'''# NOTE #'''
# 1.  If self parameter not given in method, it resulted in an 
#     error: "yash.getInfo()
#     TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given"

# 2. You need to give self parameter to method even if there is no use of it.