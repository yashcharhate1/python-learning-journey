# Q5. Write a program to Write a python function to print first n lines of the following pattern:
# ***
# **
# *

# for n = 3

def reverse_star_pattern(n):

    # i = 0
    #
    # while(i < n):
    #     print("*" * (n - i))
    #     # print("\n")
    #     i += 1
    #
    # for i in range(n):
    #     print("*" * (n - i))


    if(n == 0):
        return
    print("*" * n)
    reverse_star_pattern(n-1)

    
n = int(input("Enter the number: "))
print(reverse_star_pattern(n))