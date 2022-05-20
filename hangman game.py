#Hangman Game
#Hi! I made this lovely game and it took me only two hours. There is progress!!!
#The game uses the SOWPODS dictionary

#I have a new job and I don't have much time to learn Python now
#It's a half time job 'cause in october I'm starting my IT studies!
#New adventure, new peoples, new achievements! OH YEAH!!!

#Enjoy the game!

import random

words_list = []

with open("sowpods.txt", "r") as sowpods:
    line = sowpods.readline().strip()
    words_list.append(line)

    while line:
        line = sowpods.readline().strip()
        words_list.append(line)

hangman_pic = ["""
    +---+
    |   |
        |
        |
        |
        |
   =======""", """
    +---+
    |   |
    O   |
        |
        |
        |
   =======""", """
    +---+
    |   |
    O   |
    |   |
        |
        |
   =======""", """
    +---+
    |   |
    O   |
   /|   |
        |
        |
   =======""", """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
   =======""", """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
   =======""", """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
   ======="""]
max_tries = len(hangman_pic)-1

def hangman_game():
    random_word = random.choice(words_list)
    guess_word = "_"*len(random_word)
    random_word = list(random_word)
    guess_word = list(guess_word)
    last_guess = []
    tries = 0
    
    while tries < max_tries and guess_word != random_word:
        answer = input("Guess a letter: ")
        letter = answer.upper()
        
        while letter in last_guess:
            letter = ""
            print("You already guessed this letter! Try other letter.")
            answer = input("Guess a letter: ")
            letter = answer.upper()
            
        if letter in random_word:
            print("Correct!")
            index = random_word.index(letter)
            guess_word[index] = letter
            random_word[index] = "_"
            print("".join(guess_word))
            
        else:
            print("Incorrect!")
            print("".join(guess_word))
            tries += 1
            print(hangman_pic[tries])
            if letter != "":
                last_guess.append(letter)
            
            
    if tries == max_tries:
        print(hangman_pic[tries])
        print(f"You lose! So sad...")
    else:
        print("You're winner! Congratulations!")
        
def main():
    while True:
        if str(input("Do you want to play? yes/no: ")) == "yes":
            hangman_game()
        else:
            print("Game over. Bye bye!")
            break

main()
