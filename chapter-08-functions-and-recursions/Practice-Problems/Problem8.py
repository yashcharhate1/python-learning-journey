# Q8. Write a python function tom print multiplication table of a given number.

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

n = int(input("Enter Number: "))
print(multiplication_table(n))