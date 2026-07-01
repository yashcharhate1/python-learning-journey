# Q4. Write a Python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

path = "/Users"
contents = os.listdir(path)

print(contents)