import random as rand
guesses = 0
win = False
number = rand.randint(1,10)
guess input("Guess my number! (1-10, if you win, you get a prize!) you have 3 tries: ")
while guesses <= 3
  if guess == number:
    print("You Won! Your Prize Is:")
    prize_number = rand.randint(1,3)
    if prize number == 1:
      print("100,000,000 dollars!")
    elif prize number == 2:
      print("A new supercar!")
    else:
      print("10 Mansions!")
    win = True
  elif guess >= number:
    print("Too high!")
  else:
    print("Too low!")

if Win == True:
  print("You Won! Thanks for Playing! :D")
else:
  print("You Lost! Better luck next time :L")
print("Made by ItsBestie3434 , Re-run the script to play again!")
