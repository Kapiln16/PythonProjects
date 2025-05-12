import random
#introduction code


# number guess mechanism
x = random.randrange(100)

#chance mechanism
chance_max = 10
for chance in range (1,chance_max + 1 ):

#input mechanism
 y= int(input("Enter Your Guess :    "))

#guess mechanism
 if (y == x ):
    print(f"\nHURRAY YOUR GUESS IS CORRECT. GUESS WAS {x} and You Cracked it in {chance} chances")
    print("Thank You for playing!!")
    break

 elif (y>=x) :
    print(f"Your value is too high CHANCE NO :{chance}")

 else:
    print(f"Your value is too low. CHANCE NO :{chance}")

 if chance == chance_max :
    print(f"SORRY OUT OF CHANCES. THE NO. WAS {x}" )
    
