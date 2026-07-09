# Q4. Write a recursive function to calculate the sum of first n natural numbers.

# sum(1) = 1
# sum(2) = 1 + 2
# sum(3) = 1 + 2 + 3
# sum(4) = 1 + 2 + 3 + 4
# sum(5) = 1 + 2 + 3 + 4 + 5

# sum(n) = 1 + 2 + 3 + 4 + 5 + ........ + (n - 1) + n
# sum(n) = sum (n - 1) = n

def sum_of_natural_numbers(n):
    # sum = 0

    # for i in range(1, n+1):
    #     sum = sum + i

    if(n == 1):
        return 1

    return sum_of_natural_numbers(n - 1) + n

n = int(input("Enter the number: "))
print(f"The sum of first {n} natural numbers is: {sum_of_natural_numbers(n)}")