# Q1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter number to print Multiplication table of: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")