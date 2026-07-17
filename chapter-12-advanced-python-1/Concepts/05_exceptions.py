try:
    a = int(input("Hey! Enter the number: "))

except ValueError as v:
    print("Hey!")
    print(v)

except Exception as e:
    print(e)

print("Thank You.")
