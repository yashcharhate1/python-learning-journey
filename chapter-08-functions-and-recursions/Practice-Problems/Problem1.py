# Q1. Write a program using functions to find the greatest of three numbers.

def greatest(a, b, c):
    greatest = a

    if(b > greatest):
        greatest = b

    if(c > greatest):
        greatest = c

    return greatest


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(f"The greatest of three number is: {greatest(a, b, c)}")