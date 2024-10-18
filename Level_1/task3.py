#EMAIL VALIDATOR
#===============

import re #stands for 'regular expression', to search,match,manipulate within a string.

def is_valid_email(email):
    email_regex = re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if email_regex.match(email):
        return True
    else:
        return False
    
while True:
    email = input("Enter your email: ").strip()
    if is_valid_email(email):
        print("Email is valid")
    else:
        print("Email is not valid")

    continue_choice = input("Want to check another email address ? ('yes' to continue, 'no' to exit): ").strip().lower()
    if continue_choice != "yes":
        print("Exiting.......GoodBye!!")
        break

"""
Output
======
Enter your email: amarranjan@gmail.com
Email is valid
Want to check another email address ? ('yes' to continue, 'no' to exit): yes
Enter your email: amar48@gamil@.com
Email is not valid
Want to check another email address ? ('yes' to continue, 'no' to exit): no
Exiting.......GoodBye!!

"""