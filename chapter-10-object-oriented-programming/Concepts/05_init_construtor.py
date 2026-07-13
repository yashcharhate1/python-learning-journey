class Employee:
    language = "Python"
    salary = 1200000 

    def __init__(self, name, salary, language):     # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an Object...")  

    def getInfo(self):
        print(f"The languauge is {self.language}. And salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning!")

yash = Employee("Yash", 1300000, "JavaScript")      # must provide name, salary and language, otherwise it resulted in an error
# yash.name = "Yash"
print(yash.name, yash.salary, yash.language)