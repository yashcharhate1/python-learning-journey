marks = {
    "Anshu": 99,
    "Yash": 1,
    "Chico": 100,
    "Avantika": 69,
    "list": [13, 10, 2004]
}

name = {
    "Shambhu": 60,
    "Chivu": 70,
    "Trishika": 80
}

keys = ["Khushi", "Disha", "Muskan"]


print(marks.items())    # Returns all key-value pairs
print(marks.keys())    # Returns all the keys 
print(marks.values())    # Returns all the values 

marks.update({"Chico": 1000, "Avantika": 69})    # Updates existing key-value pairs
print(marks)

print(marks.get("Anshu"))    # Returns the value of the given key "Anshu" which is 99

print(marks.pop("Avantika"))    # Removes and returns the value of the given key "Avantika" which is 69

print(marks.popitem())    # Removes and returns the last inserted key-value pair

marks.update(name)    # Adds all key-value pairs from name dictionary tp marks dictionary
print(marks)

marks.copy()    # Creates a copy of the dictionary

marks.clear()    # Removes all items from the dictionary

new_marks = marks.fromkeys(keys, 0)    # Creates a new dictionary with given keys and a default value
print(new_marks)

