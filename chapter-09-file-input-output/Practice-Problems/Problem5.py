# Q5. Repeat program 4 for list of such words to be censored.


words = ["damn", "idiot", "bullshit", "asshole", "pissed", "jerk", "crap", "stupid"]

with open("censor.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

# print(content)

with open("censor.txt", "w") as f:
    f.write(content)
