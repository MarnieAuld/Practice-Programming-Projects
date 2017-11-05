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


def create_loading_bar(percentage, width):
    number_of_stars = int(percentage/100 * width)
    number_of_dashes = width - number_of_stars
    print("|", end='')
    for i in range(0, number_of_stars):
        print("*", end='')
    for i in range(0, number_of_dashes):
        print("-", end='')
    print("|", end='')


create_loading_bar(90, 18)
