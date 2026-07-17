a = 67

def fun():
    global a    # Can change the global variable value now.
    a = 3
    print(a)

fun()
print(a)