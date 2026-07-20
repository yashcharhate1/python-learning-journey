# Q2. Write a program to input name, marks and phone number of a student and format using the format function like below:

# "The name of the student is Yash, his marks are 72 and phone number is 9999899998"

name = input("Enter the name: ")
marks = int(input("Enter the marks: "))
phoneNumber = int(input("Enter the Phone Number: "))

student = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phoneNumber)

print(student)