import random
import time
from tkinter import Tk
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@','#','$','1','2','3','5','6','7','8','9']
i = 0


print('Welcome to PassWord Generator')
x = input("Do You want to generate password :  ")

if ( x == "yes"):
   j = int(input('Enter No. of digit in password. :  ' ))
   count = 3
   for i in range(4):
       time.sleep(1)
       print("Generating in :",count)
       count -= 1
      
       

# in for i range if we take a variable it will return value none pls fix it
   
   print('Pass Generated :')
   for i in range(j):
          generator1 = random.choice(list1)
          i+=1     
          x = print(generator1, end = "")

   print('\nThanks For Using this project!! ')

   
else:
  print('Okay!!')
  print('\nThanks For Using this project!! ')

        
      
   
