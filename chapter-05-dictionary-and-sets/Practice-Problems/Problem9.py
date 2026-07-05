# Q9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

print(type(s))



'''# Terminal Output/Error #'''

# """
# Traceback (most recent call last):
#   File "c:\Users\hp\Python Youtube Free Course - Code with Harry\Chapter 5 - PS\Problem9.py", line 4, in <module>
#     s = {8, 7, 12, "Harry", [1,2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: cannot use 'list' as a set element (unhashable type: 'list')

# """