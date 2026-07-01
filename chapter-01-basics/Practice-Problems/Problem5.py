# Q5. Label the program written in problem 4 with commetns.

import os

# Select the directory whose content you want to list
path = "/Users"

# Use the os module to list the directory content
contents = os.listdir(path)

# Print the contents of directory
print(contents)
