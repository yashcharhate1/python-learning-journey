# Q4. Write a program to filter a list of numbers which are divisible by 5.

l = [42, 7, 91, 15, 63, 28, 84, 3, 56, 19]

def div5(n):
    if(n%5 == 0):
        return True
    return False

d = filter(div5, l)
print(list(d))