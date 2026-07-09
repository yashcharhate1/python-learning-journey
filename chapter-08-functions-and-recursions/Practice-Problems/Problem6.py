# Q6. Write a python function which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54

inch = float(input("Enter the inches: "))
print(f"The {inch} inch into cms are: {inch_to_cms(inch)}")