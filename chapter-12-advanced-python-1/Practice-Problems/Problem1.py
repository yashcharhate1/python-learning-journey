# Q1. Wrte a program to open three files 1.txt, 2.txt and 3.txt if any these files or not present, a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)


# try:
#     with(
#         open("1.txt", "r") as f1,
#         open("2.txt", "r") as f2,
#         open("3.txt", "r") as f3,
#     ):
#         print(f1.read())
#         print(f2.read())
#         print(f3.read())
#
# except FileNotFoundError as e:
#     print(e)


print("Thank You!")