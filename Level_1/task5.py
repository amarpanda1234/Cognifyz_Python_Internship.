#PALINDROME CHECKER
#==================

def is_palindrome(p):
    return p == p[::-1]

while True:
    str = input("Enter the string: ")
    if is_palindrome(str):
        print (f"{str} is palindrome")
    else:
        print (f"{str} is not palindrome")

    continue_choice = input("Want to check another string ? (yes to continue, no to exit): ").strip().lower()
    if continue_choice != "yes":
        print("Exiting.......GoodBye!!")
        break

'''
OUTPUT
======
Enter the string: dad
dad is palindrome
Want to check another string ? (yes to continue, no to exit): yes
Enter the string: mom
mom is palindrome
Want to check another string ? (yes to continue, no to exit): yes
Enter the string: tech
tech is not palindrome
Want to check another string ? (yes to continue, no to exit): no
Exiting.......GoodBye!!
'''