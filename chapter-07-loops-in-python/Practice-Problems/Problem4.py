# Q4. Write a program to find whether a given number is prime or not.

n = int(input("Enter Number to check if it is Prime number or not: "))

for i in range(2, n):
    if(n % i == 0):
        print("Found a divisor, so it's not prime")
        break
    
else:
    print("It is a Prime Number")

