# Q6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assumes the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter Langauge name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter Langauge name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter Langauge name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter Langauge name: ")
d.update({name : lang})

print(d)
