# NUMBER GUESSER
# ==============

import random

def feedback(guess,number,min_num,max_num):
    range_size = max_num - min_num
    if abs(guess - number) > range_size*0.2:
        if guess < number:
            print("Too low! Try Again")
        else:
            print("Too high! Try Again")
    
    else:
        print("Low! Try Again" if guess < number else "High! Try Again")


def guess_the_number(min_num,max_num):
    number = random.randint(min_num,max_num)
    while True:
        guess = int(input(f"Guess the number between {min_num} & {max_num}: "))
        if guess == number:
            print("Congratulation!! You guessed the correct number",number)
            break
        else:
            feedback(guess,number,min_num,max_num)
    play_again = input("Want to play again (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number(min_num,max_num)
    else:
        print("Thank You for playing!!")

min_range = int(input("Enter the minimum number in the range: "))
max_range = int(input("Enter the maximum number in the range: "))
guess_the_number(min_range,max_range)

'''
OUTPUT
======
Enter the minimum number in the range: 0
Enter the maximum number in the range: 10
Guess the number between 0 & 10: 8
Too high! Try Again
Guess the number between 0 & 10: 4
High! Try Again
Guess the number between 0 & 10: 2
Congratulation!! You guessed the correct number 2
Want to play again (yes/no): no
Thank You for playing!!
'''