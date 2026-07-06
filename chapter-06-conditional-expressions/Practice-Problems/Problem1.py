# Q1. Write a program to find the greatest of the 4 numbers entered by the user.

'''# Easy Method #'''

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))
d = int(input("Enter Number: "))

if a > b and a > c and a > d:
    print("Greatest number is a:", a)

if b > a and b > c and b > d:
    print("Greatest number is b:", b)

if c > a and c > b and c > d:
    print("Greatest number is c:", c)

if d > a and d > b and d > c:
    print("Greatest number is d:", d)
    


'''# Efficient Method #'''

# a = int(input("Enter Number: "))
# b = int(input("Enter Number: "))
# c = int(input("Enter Number: "))
# d = int(input("Enter Number: "))
#
# greatest = a
#
# if b > greatest:
#     greatest = b
#
# if c > greatest:
#     greatest = c
#
# if d > greatest:
#     greatest = d
#
# print("The Greatest Number is:", greatest)