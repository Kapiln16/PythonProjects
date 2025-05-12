import random

print("Welcome To 21 Number Game \n")
print("Lets Start")


# usernum = is the input no given by user 
# compnum = is the input no given by comp
chance = 0
compvalue = 0

print("CHOOSE TURNS : ME OR COMPUTER")
choose = input()

if ( choose == "me"):
      print("Okay... Starting \n")
if (choose == 'computer'):
      turnrandom = random.randrange(1,5)
      print("Computer Value : \n",turnrandom )
      

while (compvalue <= 21):
    usernum = int(input("Enter Your No : "))
    if compvalue == usernum :
          print("Same Values are Restricted Try Again")
          break
        
    elif ( usernum):
          compvalue = random.randrange(usernum+1 ,usernum+3)
          print("Computer Value is :" , compvalue)
          chance +=1
   

    if usernum == 21 :
      print("You Lost Try again!!")
      break

    if compvalue == 21 :
         print("You Won in no. of chances", chance)
         break