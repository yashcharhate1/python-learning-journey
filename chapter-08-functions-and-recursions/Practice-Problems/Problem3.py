# Q3. How do you prevent a python print() function to print a next line at the end.

def greet(name, greeting = "Good Morning, "):
    print(f"{greeting}", end = "") # end="" : is used to prevent a python print() function to print a next line at the end.
    print(f"{name}")

name = input("Enter the name to greet them: ")
greet(name)