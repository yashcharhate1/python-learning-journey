friends = ["Apple", "Orange", "5", "345.06", "Anshu", "Yash"]

friends[5] = "loves"    # Changes the value at index 5
friends.append("Yash")    # Adds "Yash" to the end of the list

print(friends)
print(friends[4:])    # Prints the list from index 4 to the end

roll_numbers = ["61", "6542", "83", "44", "55"]

print(roll_numbers)

roll_numbers.sort()    # Sorts the list in ascending order
print(roll_numbers)

roll_numbers.reverse()
print(roll_numbers)

friends.insert(1, "Violet")    # Inserts "Violet" at index 1
print(friends)

print(roll_numbers.pop(2))    # Removes and returns the element at index 2

friends.remove("Violet")    # Removes "Violet" from the list
print(friends)