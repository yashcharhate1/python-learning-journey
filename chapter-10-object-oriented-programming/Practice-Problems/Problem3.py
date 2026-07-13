# Q3. Create a class of class attribute a; creat an object from it and set 'a' directly using object. a = 0. Does this change the class attribute.

class Demo:
    a = 13  # This is a class attribute

obj = Demo()
print(obj.a)    # This prints class attribute because instance attribute is not present.
obj.a = 0   # This is an Instance attribute
print(obj.a)    # This prints instance attribute because instance attribute is present.


''' If we written like following we still get class attribute value '''

print(Demo().a) # We still get 13 as value