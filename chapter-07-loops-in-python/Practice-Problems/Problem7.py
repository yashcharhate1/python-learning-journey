# Q7. Write a program to print the following star pattern.
#   *
#  ***
# *****       for n = 3


n = int(input("Enter number: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i - 1), end="")
    print("\n")



# for reverse pattern

# *****       for n = 3
#  ***
#   *

j = n
while(j >= 1):
    print(" " * (n-j), end="")
    print("*" * (2*j - 1), end="")
    print("\n")
    j = j - 1
    