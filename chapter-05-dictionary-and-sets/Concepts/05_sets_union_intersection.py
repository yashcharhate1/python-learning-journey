s1 = {51, 2, 73, 34, 3}
s2 = {2, 5, 58, 51, 8}
s3 = {2, 3}
s4 = {5, 8}

print(s1.union(s2))    # Returns a new set containing all unique elements from both sets

print(s1.intersection(s2))    # Returns the common elements in both sets

print(s1.difference(s2))    # Returns elements that are in s1 but not in s2

print(s2.difference(s1))    # Returns elements that are in s2 but not in s1

print(s2.symmetric_difference(s1))    # Returns elements that are in either set but not in both

print(s3.issubset(s1))    # Checks if s3 is a subset of s1

print(s1.issuperset(s3))    # Checks if s1 is a superset of s3

print(s1.isdisjoint(s4))    # Checks if both sets have no common elements