# FIBONACCI SEQUENCE
# ==================

def fibonacci_seq(terms):
    fibonacci_sequence = [0,1]

    for i in range(2,terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence\
    
while True:
    terms = int(input("Enter the number of terms for fibonacci sequence: "))
    if terms <= 0:
        print("Please enter a positive number")
        continue
    else:
        fib_sequence = fibonacci_seq(terms)
        print("Fibonacci Sequence upto",terms,"terms: ",*fib_sequence)
        again = input("Do you want to calculate again ? (yes/no): ").lower()
        if again == "yes":
            continue
        else:
            print("Thank you for using fibonacci Sequence")
            break

'''
OUTPUT
======
Enter the number of terms for fibonacci sequence: 5
Fibonacci Sequence upto 5 terms:  0 1 1 2 3
Do you want to calculate again ? (yes/no): yes
Enter the number of terms for fibonacci sequence: 10
Fibonacci Sequence upto 10 terms:  0 1 1 2 3 5 8 13 21 34
Do you want to calculate again ? (yes/no): no
Thank you for using fibonacci Sequence
'''