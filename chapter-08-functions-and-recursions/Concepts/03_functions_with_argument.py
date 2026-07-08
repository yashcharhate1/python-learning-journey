'''# Function with Arguments #'''

def goodDay(name, ending):
    print("Good Day! " + name)
    print(ending)

goodDay("Yash", "Dhanyawaad")
goodDay("Anshulika", "Thank You")
goodDay("Khushi", "Thanks")
goodDay("Chico", "Arigato")



def goodDay(name, ending):
    print("Good Day! " + name)
    print(ending)
    return "That's all"

a = goodDay("Yash", "Dhanyawaad")
print(a)