import random as rand
comp_choice = rand.randint(1,3)
choice = input("Choose rock, paper, or scissors")
if comp_choice == 1:
  print("I choose rock!")
elif comp_choice == 2:
  print("I choose paper!")
else:
  print("i choose scissors!")
if choice == "rock" and comp_choice == 1:
  print("it's a draw!")
elif choice == "rock" and comp_choice == 2:
  print("computer wins!")
elif choice == "rock" and comp_choice == 3:
  print(player wins!")
elif choice == "paper" and comp_choice == 1:
  print("player wins!")
elif choice == "paper" and comp_choice == 2:
  print("it's a draw!")
elif choice == "paper" and comp_choice == 3:
  print("player wins!")
elif choice == "scissors" and comp_choice == 1:
  print("computer wins!")
elif choice == "scissors" and comp_choice == 2:
  print("player wins!")
elif choice == "scissors" and comp_choice == 3:
  print("it's a draw!")
else:
  print("unknown")
print("thanks for playing! re-run script to try again!")



