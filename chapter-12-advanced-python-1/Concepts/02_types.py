# Variable type hints
n : int = 13


name : str = "Yash"

# Function type hints
def sum(a: int, b: int) -> int:
    return a + b

print(sum(3, 4))



# ------------------------------------------------------------------------------------------------------------------------------ #



''' Advanced type hints'''

from typing import List, Tuple, Dict, Union

# List of integers
numbers : List[int] = [1, 2, 3, 4, 5]

# print(type(numbers))

# Tuple of a string and an Integer
person : Tuple[str, int] = ("Anshu", 22)

# Dictionary with string keys and an Inter=ger values
scores : Dict[str, int] = {"Anshu" : 99, "Yash" : 1}

# Union type for variable that can be hold multiple types
identifier : Union[str, int] = "ID123"
identifier = 12345      # Also valid


'''# These annotations help in making the code self-documentiog and allow developers to understand the data structure used at glance. #'''
