# Dictionary Merge and Update Operators

dict1 = {
    "a" : 1,
    "b" : 2
}

dict2 = {
    "b" : 3,
    "c" : 4
}

merged = dict1 | dict2

print(merged)   # Output: {'a': 1, 'b': 3, 'c': 4}

# ------------------------------------------------------------------------------------------------------------------------------ #

"""# Additional File functions #"""

# We can use multiple files with "with function"
with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    print(f1.read())
    print(f2.read())
    # Processed files