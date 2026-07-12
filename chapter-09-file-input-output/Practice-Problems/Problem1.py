# Q1. Write the program to read the text from a given file "poem.txt" and find out whether it contains the word "twinkle".

# open "poem.txt" file
f = open("poem.txt")

# read the content
content = f.read()

# check if word "twinkle" is present in file
if("twinkle" in content.lower()):
    print("The word 'twinkle' is present in the File content.")
else:
    print("The word 'twinkle' is not present in the File content.")

# close file
f.close()
