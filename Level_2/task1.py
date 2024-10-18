#GUESSING GAME
#=============

import random

def guess_number():
    number = random.randint(1,100)
    while True:
        guess = int(input("Guess the number between 1 to 100: "))
        if guess == number:
            print("Congratulation!! You guessed correct number",number)
            break
        elif guess < number:
            print("Too low! Try Again")
        else:
            print("Too high! Try Again")
    play_again = input("Want to play again ? (yes/no): ").lower()
    if play_again == "yes":
        guess_number()
    else:
        print("Thank You for playing!")
guess_number()

'''
OUTPUT
======
Guess the number between 1 to 100: 50
Too high! Try Again
Guess the number between 1 to 100: 40
Too high! Try Again
Guess the number between 1 to 100: 30
Too high! Try Again
Guess the number between 1 to 100: 10
Too low! Try Again
Guess the number between 1 to 100: 13
Too low! Try Again
Guess the number between 1 to 100: 20
Too low! Try Again
Guess the number between 1 to 100: 30
Too high! Try Again
Guess the number between 1 to 100: 25
Too high! Try Again
Guess the number between 1 to 100: 22
Too low! Try Again
Guess the number between 1 to 100: 23
Too low! Try Again
Guess the number between 1 to 100: 24
Congratulation!! You guessed correct number 24
Want to play again ? (yes/no): no
Thank You for playing!
'''