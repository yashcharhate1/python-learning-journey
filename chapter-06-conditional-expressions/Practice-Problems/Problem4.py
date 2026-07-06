# Q4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Username: ")

if(len(username) < 10):
    print("Username contains less than 10 characters.")

elif(len(username) == 10):
    print("Username contains 10 characters.")

else:
    print("Username contains more than 10 characters.")