try:
    a = int(input("Hey! Enter the number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I'm inside else")    # Else block executed only if the try was successful
