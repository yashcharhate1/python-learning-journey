# Q3. Create a class 'Employee' and add salary and increament properties to it.

# Write a method 'salaryAfterIncrement' method with @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return int(self.salary + (self.salary *(self.increment/100)))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

# employeeObj = Employee(80000, 20)
# print(employeeObj.salaryAfterIncrement)

employeeObj = Employee(80000, 20)
employeeObj.salaryAfterIncrement = 96000
print(employeeObj.increment)