#CALCULATOR PROGRAM
#==================

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error: Division by ZERO is not possible"
    
def modulo(x,y):
    return x%y


while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator(+, -, *, /, %): ").strip()

    if operator == "+":
        result = add(num1,num2)
    elif operator == "-":
        result = subtract(num1,num2)
    elif operator == "*":
        result = multiply(num1,num2)  
    elif operator == "/":
        result = divide(num1,num2)
    elif operator == "%":
        result = modulo(num1,num2)
    else:
        print("Error: Invalid Operator")

    print(f"The result of {num1} {operator} {num2} is: {result}")

    continue_choice = input("Want to perform another calculation ? (yes to continue, no to exit): ").strip().lower()
    if continue_choice != "yes":
        print("Exiting.......Goodbye!!")
        break

'''
OUTPUT
------
Enter first number: 4
Enter second number: 5
Enter an operator(+, -, *, /, %): +
The result of 4.0 + 5.0 is: 9.0
Want to perform another calculation ? (yes to continue, no to exit): yes
Enter first number: 2
Enter second number: 3
Enter an operator(+, -, *, /, %): *
The result of 2.0 * 3.0 is: 6.0
Want to perform another calculation ? (yes to continue, no to exit): yes
Enter first number: 7
Enter second number: 1
Enter an operator(+, -, *, /, %): -
The result of 7.0 - 1.0 is: 6.0
Want to perform another calculation ? (yes to continue, no to exit): yes
Enter first number: 10
Enter second number: 5
Enter an operator(+, -, *, /, %): /
The result of 10.0 / 5.0 is: 2.0
Want to perform another calculation ? (yes to continue, no to exit): yes
Enter first number: 100
Enter second number: 10
Enter an operator(+, -, *, /, %): %
The result of 100.0 % 10.0 is: 0.0
Want to perform another calculation ? (yes to continue, no to exit): yes
Enter first number: 9
Enter second number: 0
Enter an operator(+, -, *, /, %): /
The result of 9.0 / 0.0 is: Error: Division by ZERO is not possible
Want to perform another calculation ? (yes to continue, no to exit): no
Exiting.......Goodbye!! '''