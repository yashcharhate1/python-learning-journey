a = int(input("Enter Your Age: "))

# If Statement no. 1
if(a%2 == 0):
    print("a is even")

# End of If Statement no. 1

# If Statement no. 2

if(a>=18):
    print("You're above the age of consent")
    print("Good for you")

elif(a<0):
    print("You're entering invalide negative age.")

elif(a==0):
    print("You're entering \"0\" which is Invalid Age.")

else:
    print("You're below the age of consent")

# End of If Statement no. 2

print("End of the Program")