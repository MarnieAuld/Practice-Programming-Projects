"""
Selection Programming Practice
"""

"""
Write a program to check if someone can vote. They need to be 18 or over and be enrolled to vote.
You could do two versions - one with nested ifs and one with the 'and' operator.
"""
# age = int(input("Enter your age: \n>>> "))
# if age >= 18:
#     enrolled_to_vote = input("Are you enrolled to vote? y/n \n>>>").lower()
#     if enrolled_to_vote == "y":
#         print("You can vote!")
#     else:
#         print("You need to enrol to be eligible to vote")
# else:
#     print("You are too young to vote")

"""
Write the Kebab Kalkulator: The program should have base prices for small ($7.50) or large ($10) kebabs (constants).
The user should choose a size, and how many extra toppings they want: 
up to 2 toppings are free, 3 or more toppings are 50c each (but not counting the free ones!).
Examples:
a small kebab with 3 toppings = $8
a large kebab with 2 toppings = $10
large with 10 = $14
Ask the user for their options, then print the final price.
"""
"""
Write a program which asked a user for SIZE and NUMBER OF TOPPINGS and return the final price.
"""

SMALL_KEBAB = 7.50
LARGE_KEBAB = 10
TOPPING_PRICE = 0.50
NUMBER_OF_FREE_TOPPINGS = 2


def main():
    kebab_price = get_kebab_size() + get_number_of_toppings()
    print("Kebab price = {:.2f}".format(kebab_price))


def get_kebab_size():
    kebab_size = input("What size kebab do you require? SMALL or LARGE").upper()
    if kebab_size == "SMALL":
        kebab_size = SMALL_KEBAB
    elif kebab_size == "LARGE":
        kebab_size = LARGE_KEBAB
    else:
        print("Invalid Input")
        kebab_size = input("What size kebab do you require? SMALL or LARGE").upper()
    return kebab_size


def get_number_of_toppings():
    try:
        number_of_toppings = int(input("How many toppings do you require?"))
        if number_of_toppings <= NUMBER_OF_FREE_TOPPINGS:
            topping_charge = 0
        else:
            topping_charge = TOPPING_PRICE * (number_of_toppings - NUMBER_OF_FREE_TOPPINGS)
    except ValueError:
        print("Invalid input; please enter a valid number")
        number_of_toppings = int(input("How many toppings do you require?"))
    return topping_charge


main()
