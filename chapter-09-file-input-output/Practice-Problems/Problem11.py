# Q.11 Write a python program to rename a file tp "renamed_by_python.txt".

with open("old.txt") as f:
    content = f.read()

with open("rename_by_python.txt", "w") as f:
    f.write(content)

# Then you need to delete the file "old.txt" using "OS" and "shutil" module.