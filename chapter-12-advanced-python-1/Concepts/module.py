def myFunc():
    print("Hello! World")

myFunc()
print(__name__)   

# ------------------------------------------------------------------------------------------------------------------------------ #

# If print(__name__) is run in module.py it return "__main__" as Output.
# If this run in 09_main.py it returns the file where the main code lies. # Output: "module"

# print(__name__) used to check whether the module is run directly or imported to the another file.

# ------------------------------------------------------------------------------------------------------------------------------ #

def myFunc():
    print("Hello! World")

if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code.")
    myFunc()
    print(__name__) 