# Q7. If the names of 2 friends are same; what will happen to the program in problem 6.

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



'''# Terminal Output #'''

# """
# Enter friends name: Yash
# Enter Langauge name: Python
# Enter friends name: Anshulika
# Enter Langauge name: Python
# Enter friends name: Khushi
# Enter Langauge name: Java
# Enter friends name: Khushi 
# Enter Langauge name: CPP
# {'Yash': 'Python', 'Anshulika': 'Python', 'Khushi': 'CPP'}          #It will Update the value of the same key if enter again later.

# """