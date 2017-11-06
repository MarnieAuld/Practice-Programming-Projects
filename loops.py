"""
Loops Programming Practice
"""

"""
Write a menu-driven program that loops until the user quits. 
The options are (G)et name, (U)ppercase, (L)owercase, (Q)uit.
The program should start by asking the user for their name before the menu, but they can (G)et a new name. 
U/L print the name in either uppercase or lowercase.
"""

# MENU = "(G)et name \n(U)ppercase \n(L)owercase \n(Q)uit"
# user_name = input("Enter your name: ")
# print(MENU)
# user_choice = input(">>> ").upper()
# while user_choice != "Q":
#     if user_choice == "G":
#         user_name = input("Enter your name: ")
#     elif user_choice == "U":
#         print(user_name.upper())
#     else:
#         print(user_name.lower())
#     print(MENU)
#     user_choice = input(">>> ").upper()
# print("Catchya")


"""
Print the square of numbers between a given range. 
Ask the user for a lower number and a higher number..
.. then print all of the squares of the numbers in that range (inclusive).
Error-check the second number to make sure it is higher than the first.
"""
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# if number1 > number2:
#     print("Second number cannot be larger than first number")
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
# for i in range(number1, number2 + 1, 1):
#     print(i*i)


"""
Print a "progress bar" based on a percentage (number). 
E.g. 50% would print something like: |*****-----|, 10% would print |*---------|
Modify your previous progress bar code so you can specify a width for the bar 
(if using a function, pass in the percentage and width). E.g. 50% of 18 would be:|*********---------|
"""
#
#
# def create_loading_bar(percentage, width):
#     number_of_stars = int(percentage/100 * width)
#     number_of_dashes = width - number_of_stars
#     print("|", end='')
#     for i in range(0, number_of_stars):
#         print("*", end='')
#     for i in range(0, number_of_dashes):
#         print("-", end='')
#     print("|", end='')
#
#
# create_loading_bar(90, 18)


"""
Write a program that prompts for an integer and prints the integer,
but if something other than an integer is input, the program keeps asking for an integer.
SAMPLE OUTPUT
    Input an integer: abc
    Error: try again. Input an integer: 4a
    Error: try again. Input an integer: 2.5
    Error: try again. Input an integer: 123
    The integer is: 123
"""
# user_input = input("Input an integer: ")
# while not user_input.isdigit():
#     user_input = input("Error: try again. Input an integer: ")
# if user_input is float:
#     user_input = input("Error: try again. Input an integer: ")
# else:
#     print("The integer is: {}".format(user_input))


"""
Create a program that prompts for a positive number greater than 2, then keeps taking the square root
of this number until the square root is less than 2.
Print the value each time the square root is taken, 
along with the number of times the operation has been completed (USE STRING FORMATTING)
"""
from math import sqrt

user_integer = int(input("Input an integer: "))
while user_integer < 2:
    print("Error - Integer must be more than 2")
    user_integer = int(input("Input an integer: "))
operation_count = 1
square_root = sqrt(user_integer)
print("{}: {:.3f}".format(operation_count, square_root))
while not square_root < 2:
    operation_count += 1
    square_root = sqrt(square_root)
    print("{}: {:.3f}".format(operation_count, square_root))