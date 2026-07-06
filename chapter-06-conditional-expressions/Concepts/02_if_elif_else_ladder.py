a = int(input("Enter Your Age: "))

# If elif else ladder

if(a>=18):
    print("You're above the age of consent")
    print("Good for you")

elif(a<0):
    print("You're entering invalide negative age.")

elif(a==0):
    print("You're entering \"0\" which is Invalid Age.")

else:
    print("You're below the age of consent")

print("End of the Program")