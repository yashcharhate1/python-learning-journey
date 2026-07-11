# Open File
f = open("file.txt")

# To print lines in file (It is printed in 'List' format 
lines = f.readlines()
print(lines, type(lines))

# To print First line of Paragraph in file 
line1 = f.readline()
print(line1, type(line1))

# To print Second line of Paragraph in file 
line2 = f.readline()
print(line2, type(line2))

# To print Third line of Paragraph in file 
line3 = f.readline()
print(line3, type(line3))

# To print Fourth line of Paragraph in file 
line4 = f.readline()
print(line4, type(line4))


# To print all lines of Paragraph one by one in file Using Loop 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

# File Close
f.close()