#TEMPERATURE CONVERSION
#======================

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("Enter 'C' for celcius or 'F' for fahrenheit")

    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = celcius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celcius(temp)
        print(f"{temp}°F is equal to {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for celcius or 'F' for fahrenheit")

    continue_choice = input("Want to perform another temperature conversion ? ('yes' to continue, 'no' to exit): ")
    if continue_choice != "yes":
        print("Exiting.......GoodBye!!")
        break

"""
Output
======

Enter 'C' for celcius or 'F' for fahrenheit
Enter the temperature value: 40
Enter the unit of measurement (C/F): C
40.0°C is equal to 104.0°F
Want to perform another temperature conversion ? ('yes' to continue, 'no' to exit): yes
Enter 'C' for celcius or 'F' for fahrenheit
Enter the temperature value: 102
Enter the unit of measurement (C/F): f
102.0°F is equal to 38.888888888888886°C
Want to perform another temperature conversion ? ('yes' to continue, 'no' to exit): no
Exiting.......GoodBye!!

"""