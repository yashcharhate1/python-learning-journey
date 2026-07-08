''' Instead of repitation of same code '''

# a = int(input("Enter Your Number: "))
# b = int(input("Enter Your Number: "))
# c = int(input("Enter Your Number: "))
#
# average = (a+b+c)/3
# print(average)
#
# a = int(input("Enter Your Number: "))
# b = int(input("Enter Your Number: "))
# c = int(input("Enter Your Number: "))
#
# average = (a+b+c)/3
# print(average)
#


''' We put the single code in Function. And Function can call multiple times. '''

## Function Defination: Where function is defined

def avg():
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = int(input("Enter Your Number: "))

    average = (a+b+c)/3
    print(average)

## Function Call

avg()
avg()
avg()
avg()
avg()