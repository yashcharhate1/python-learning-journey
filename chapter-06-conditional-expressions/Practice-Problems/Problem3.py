# Q3. A spam comment is defined as a text containing following keywords:
# *Make a lot of money*, *Buy now*, *Suscribe this*, *Click this*.
# Write a program to detect this spams.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "suscribe this"
p4 = "click this"

messege = input("Enter the Messege: ").lower()

if((p1 in messege) or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("This comment is a spam.")

else:
    print("This comment is not a spam.")