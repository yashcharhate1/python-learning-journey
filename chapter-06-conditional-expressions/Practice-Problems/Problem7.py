# Q7. Write a program to finds out whether a given post is talking about "Yash" or not.

post = input("Enter post: ").lower()

if("Yash".lower() in post):
    print("The post is talking about Yash.")

else:
    print("The post is not talking about Yash.")