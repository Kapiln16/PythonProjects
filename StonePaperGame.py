import time
import random

def load():
    count = 3
    for el in range(3):
     
     print("Loading :", count )
     time.sleep(0.1)
     count -= 1
    return 'Loaded'

complist = ['stone','scissor','paper']
compvalue = random.choice(complist)
result = ''
print("Welcome To Stone Paper Game!\n")
time.sleep(1)
print("Rules as follows:\nRock vs paper : paper wins\nRock vs scissor : Rock wins\npaper vs scissor : scissor wins.")
time.sleep(1)
toplay = input("Do you Want to play :  ")
time.sleep(1)

while (toplay == "yes"):
    print("\nChoices :\n 1.Scissor\n 2.Stone\n 3.Paper")
    time.sleep(.1)
    choice = (input('Enter Your Choice :   '))
    print("\nYour Choice :  ", choice)
    print(load())


    if(choice == compvalue):
        result = 'draw'
        
    elif(choice == "paper" and compvalue == "rock") or (choice == "rock" and compvalue == "paper" ):
        result = 'paper'
    elif(choice == "scissor" and compvalue == "paper") or (choice == "paper" and compvalue == "scissor" ):
        result = 'scissor'
    elif(choice == "stone" and compvalue == "scissor") or (choice == "scissor" and compvalue == "stone"):
        result = 'stone'


    if(result == 'paper'):
        if(choice == result):
           print('\nYou Won!!','Computer Choice :', compvalue)
        else:
            print('\nYou Lost!! Computer Won','Computer Choice :', compvalue)
    
    
    if(result == 'scissor'):
        if(choice == result):
           print('\nYou Won!! Computer Choice :', compvalue)
        else:
            print('\nYou Lost!! Computer Won','Computer Choice :', compvalue)

    
    if(result == 'stone'):
        if(choice == result):
           print('\nYou Won!!','Computer Choice :', compvalue)
        else:
            print('\nYou Lost!! Computer Won','Computer Choice :', compvalue)
    if(result == 'draw'):
        print('Draw!! Try Again')

    
    print('\nWant to Play More?')
    asktoplay = input('Answer in y or n :  ').lower()
    if asktoplay == 'n':
        print('Thanks For playing!!')
        time.sleep(1)
        print("\nProject by Kapil......")
        break
        


        
