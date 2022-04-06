#Rock-Paper-Scissors game

print("Hello! \nIt's time to play!")
print("\nThis is Rock-Paper-Scissors Game. \nYou'll play with a computer")
print("You can stop the game at any moment or you can play...")
print("\nforever :D")

import random

while True:
    choice_gamer = input("\nYour choice: ")
    choice_pc = random.randint(1, 3)
    if choice_pc == 1:
        print("Computer choice: scissors")
        if choice_gamer == "scissors":
            print("It's a tie!")
        if choice_gamer == "rock":
            print("You win!")
        if choice_gamer == "paper":
            print("You lose!")
        if str(input("Try again? yes/no: ")) == "yes":
            continue
        else:
            print("Game over")
        break
    if choice_pc == 2:
        print("Computer choice: rock")
        if choice_gamer == "rock":
            print("it's a tie!")
        if choice_gamer == "paper":
            print("You win!")
        if choice_gamer == "scissors":
            print("You lose!")
        if str(input("Try again? yes/no: ")) == "yes":
             continue
        else:
           print("Game over")
        break
    if choice_pc == 3:
        print("Computer choice: paper")
        if choice_gamer == "paper":
            print("It's a tie!")
        if choice_gamer == "scissors":
            print("You win!")
        if choice_gamer == "rock":
            print("You lose!")
        if str(input("Try again? yes/no: ")) == "yes":
             continue
        else:
            print("Game over")
        break
