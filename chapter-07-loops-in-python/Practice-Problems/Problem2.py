# Q2. Write a program to great all the person names stored in a list "l" and which starts with A.
# l = ["Yash", "Anshulika", "Khushi", "Avinya"]

l = ["Yash", "Anshulika", "Khushi", "Avinya"]



'''# Mine Complex logic 🫠 #'''

for i in range(len(l)):
    if(l[i][0].lower() == "a"):
        print(f"Hello! {l[i]}")



'''# Simple logic #'''

for name in l:
    if(name.startswith("A")):
        print(f"Hello! {name}")