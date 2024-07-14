'''
1 for rock
-1 for paper 
0 for scissor
'''
import random

choices = [-1,1,0]

computer  = random.choice(choices)

print("Game is started")
you = input("Enter:")
youDict = {"r":1,"p":-1,"s":0}
youNum = youDict[you.lower()]
reverseDict = {1:"rock",-1:"paper",0:"scissor"}

print(f"You chose {reverseDict[youNum]} & computer chose {reverseDict[computer]}")

if(computer == youNum):
  print("Its a draw")

else:
  if(computer == -1 and youNum == 1):
    print("Computer Won!! Try Again")
  elif(computer == -1 and youNum == 0):
    print("You Won!! Congo")
  elif(computer == 1 and youNum == -1):
    print("You Won!! Congo")
  elif(computer == 1 and youNum == 0):
    print("Computer Won!! Try Again")
  elif(computer == 0 and youNum == -1):
    print("Computer Won!! Try Again")
  elif(computer == 0 and youNum == 1):
    print("You Won!! Congo")
  else:
    print("Something went wrong...")
 
    