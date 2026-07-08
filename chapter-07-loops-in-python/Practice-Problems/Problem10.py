# Q.10 Write a program to print the multiplication table of n using for loops in reversed order.

n = int(input("Enter number to print Multiplication table of: "))

for i in range(1,11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")