# Q7. Write a program to find out the line number where python is present from Q.6

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if("python" in line):
        print(f"The word 'python' is present in log file at Line No. {lineno}.")
        break
    lineno += 1

else:
    print("The word 'python' is not present in log file.")