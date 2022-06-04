# Write a pyhton code, which is a number guessing game that tries to find the number that will be randomly selected from the number sequence from 1 to 100. and

#indicate in the code that each user has the right to guess 5, deduct 1 right for each wrong guess


import random
num=random.randint(1,100)
guess=5
while guess>0:
  user=int(input("Guess the my number : "))
  if user>num:
    print("You should reduce!")
    guess-=1
  elif user <num:
    print("You should increase!")
    guess-=1
  else:
    print("Weldone! You find")
    guess=0
  if guess==0:
    print("You have no more chance", num)
  elif guess==1:
    print("Be careful, you have one last chance left.")
    
    
    
    
    ### You can use break ###
    
import random
num=random.randint(1,100)
guess=5
while True:
  user=int(input("Guess the my number : "))
  if user>num:
    print("You should reduce!")
    guess-=1
  elif user <num:
    print("You should increase!")
    guess-=1
  else:
    print("Weldone! You find")
    break
  if guess==0:
    print("You have no more chance", num)
    break
  elif guess==1:
    print("Be careful, you have one last chance left.")
    
    
    
    
    
    


