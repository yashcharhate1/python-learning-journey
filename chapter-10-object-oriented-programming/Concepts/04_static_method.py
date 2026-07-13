class Employee:
    language = "Python"
    salary = 1200000   

    def getInfo(self):
        print(f"The languauge is {self.language}. And salary is {self.salary}")

    # As greet function does not use self parameter. So to prevent passing this is object we use Static method.
    @staticmethod       # decorator to mark greet as static method
    def greet(self):
        print("Good Morning!")

yash = Employee()
yash.language = "JavaScript"

yash.greet()
yash.getInfo()
