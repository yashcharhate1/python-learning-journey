f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
# So you don't have to explicitly close the file

with open("file.txt") as f:
    print(f.read())