# Shortened version of Snake-Water-Gun Game using dict-based logic instead of if/elif chains

import random

"""

1 for Snake
-1 for Water
0 for Gun

"""

computer = random.choice([-1, 0, 1])

youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

reverseDict = {
    1 : "Snake",
    -1 : "Water",
    0 : "Gun"
}

youStr = input("Enter Your Choice: ")

you = youDict[youStr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    
    '''
        if(computer == -1 and you == 1):          (computer - you) = -2
            print("You Win!")
        
        elif(computer == -1 and you == 0):        (computer - you) = -1
            print("You Lose!")
        
        elif(computer == 1 and you == -1):        (computer - you) = 2
            print("You Lose!")
        
        elif(computer == 1 and you == 0):         (computer - you) = 1
            print("You Win!")
        
        elif(computer == 0 and you == -1):        (computer - you) = 1
            print("You Win!")
        
        elif(computer == 0 and you == 1):         (computer - you) = -1
            print("You Lose!")

        else:
            print("Something went wrong!")

    '''

    
    if((computer - you) == 1 or (computer - you) == -2):
        print("You Win!")
    
    elif((computer - you) == -1 or (computer - you) == 2):
        print("You Lose!")
    
    else:
        print("Something went wrong!")