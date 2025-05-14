import random
import time

wordlist = ["Innovation", "Harmony", "Curiosity", "Velocity", "Tranquility", "Adventure", "Resilience", "Luminosity", "Momentum"]
computerguess = random.choice(wordlist) 

print("Welcome To Word Guess Game!!")
time.sleep(1)
print("\nInstruction : Max chance = 7 and Enter your guess. READ ALL WORDS \n")
print("\nWords : \nInnovation, Harmony, Curiosity, \nVelocity, Tranquility, Adventure, \nResilience, Luminosity, Momentum\n")
time.sleep(3)
play = input("Do you wanna play? :    ")
max_chance = 7

if(play == "yes"):


   for chance in range(1,max_chance,+1):

     userinput = input("Enter Your Word Guess :    ")
     computer_guess = computerguess.lower()
    
     if (userinput == computer_guess):
          print(f'You Won your guess {userinput} is correct and computer guess was {computerguess} ')
          print(f'No. of chances you took : {chance}')
          break
    
     elif ( userinput != computer_guess):
          print(f'Try again! Chance Left :{max_chance - chance}')
    
     if chance ==  max_chance:
        print(f"SORRY OUT OF CHANCES. THE Word Guess Was {computerguess}" )
        break

if(play == "no"):
    print("Lets Play anytime later!!!!!!!!!!")
    
    
    
          

         



