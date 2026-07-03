# Q2. Write a python Program to fill in a letter template given below with name and date.
# letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
# '''

letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''

name = input("Enter Name: ")
date = input("Enter Date: ")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)