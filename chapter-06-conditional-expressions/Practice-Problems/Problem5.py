# Q5. Write a program to which finds out whether a given name present in the list or not.

names = ["Anshulika", "Yash", "Vaishnavi", "Khushi", "Aarav", "Advika", "Aaradhya", "Drishti", "Trishika", "Tridham"]

name = input("Enter name: ")

if name in names:
    print(f"{name} is present in a list.")

else:
    print(f"{name} is not present in a list.")