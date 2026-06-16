import art
import random
def num_guessing_game():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I am guessing a number between 1-100")
    select=random.randint(1,100)
    level=input("Choose a difficulty. Type \'easy\' or \'hard\':")

    if level=="easy":
        lives=10
    else:
        lives=5
    while lives>0:
        print(f"You have {lives} number of attempts left to guess.")
        guess=int(input("Make a guess:"))
        if select<guess:
            print("Too high!")
            print("Guess again")
            lives-=1
        elif select>guess:
            print("Too low!")
            print("Guess again")
            lives -= 1
        else:
            print(f"You got it the answer was {select}")
            return
    print("You've run out of guesses. You lose.")

num_guessing_game()





