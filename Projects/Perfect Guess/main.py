from random import randint

correctNum = randint(1,100)
userNum = -1
guesses = 1
# print(f"correctNum is: {correctNum}")

while(userNum!=correctNum):
  
  userNum = int(input("Guess The Number: "))

  if(userNum > correctNum):
    print("Lower Number Please")
    guesses+=1
  elif(userNum < correctNum):
    print("Higher Number Please")
    guesses+=1

print(f"You have correctly guessed the number {correctNum} in {guesses} attempts")