""" DO IT NOW class examples from CP1404"""

""" 
DO IT NOW #1 
Write code that asks a user for their age and tells them if they are an adult or child
"""
# user_age = int(input("What is your age: "))
# if user_age >= 18:
#     print("You are an adult")
# else:
#     print("You are a child")

"""
DO IT NOW #2
Write code for a program to repeatedly ask the user for a number then print that number squared.
When the user enters zero or a negative number, stop.
"""
# user_number = int(input("Enter a number: "))
# while user_number > 0:
#     print(user_number*user_number)
#     user_number = int(input("Enter a number: "))

"""
DO IT NOW #3
Write a program to calculate the average age of a group of people, of unknown size. 
Use a negative number as the sentinel.
"""
# total_age = 0
# number_of_people = 0
# user_age = int(input("Enter your age: "))
# while user_age >= 0:
#     number_of_people += 1
#     total_age += user_age
#     user_age = int(input("Enter your age: "))
# print(int(total_age / number_of_people))

"""
DO IT NOW #4
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number,
The program should not allow an invalid age number, and
The program should re-prompt until a valid number is entered.
"""
# valid_input = False
# while not valid_input:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             print("Age must be positive number - how can a fetus use a computer?")
#         else:
#             valid_input = True
#             if age % 2:
#                 print("ODD")
#             else:
#                 print("EVEN")
#     except ValueError:
#         print("Invalid Input - Try Again")
#         age = int(input("Enter your age"))

"""
DO IT NOW #5
Ask the user for their name, and tell them how many vowels are in their name
"""
# VOWELS = ["a", "e", "i", "o", "u"]
# total_character_count = 0
# vowel_count = 0
# user_name = input("Enter your name: ")
# for character in user_name.lower():
#     total_character_count += 1
#     if character in VOWELS:
#         vowel_count += 1
# print("Out of {} letters, {} has {} vowels".format(total_character_count, user_name, vowel_count))

"""
DO IT NOW #6
Write a for loop that prints Olympic years (every 4 years) from 1900 to now
"""
# for i in range(1900, 2017, 4):
#     print(i)

"""
DO IT NOW #7
Write a function that returns the average value of a list of numbers passed in to it
"""
# def get_average_value(numbers):
#     total_value_numbers = 0
#     number_of_numbers = 0
#     for number in numbers:
#         total_value_numbers += int(number)
#         number_of_numbers += 1
#     return total_value_numbers / number_of_numbers
# numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# print(get_average_value(numbers))

"""
DO IT NOW #8
Write a function that returns the median value (middle when sorted) of a list of numbers passed in to it
"""
# def median(numbers):
#     n = len(numbers)
#     sorted_numbers = sorted(numbers)
#     if n % 2:
#         return sorted_numbers[n//2]
#     else:
#         return (sorted_numbers[n//2] + sorted_numbers[n//2] - 1) / 2.0
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = [2, 1, 4, 1]
# numbers3 = [0, 9, 2, 9, 5, 8, 6]
# print(median(numbers1))
# print(median(numbers2))
# print(median(numbers3))

"""
DO IT NOW #9
Write code for a function that takes two lists:
    ~ A list of names
    ~ A corresponding list of ages
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age).
"""
# def get_oldest_name(names, ages):
#     return names[ages.index(max(ages))]
# names = ["Adam", "Barry", "Craig"]
# ages = [23, 56, 33]
# print(get_oldest_name(names, ages))

"""
DO IT NOW #10
Write a list comprehension to produce a new list containing only the products that are on sale.
(TRUE means its on sale)
"""
# products = [["Phone", 240, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
# on_sale_products = {name for name, price, on_sale in products if on_sale}
# print(on_sale_products)

"""
DO IT NOW #11
Write a user class for a Hey Taco simulation. 
The user knows: name, number of tacos (starts at 5 and goes down when they give a taco) and their score.
A user can give a taco to another user.
Should be able to print a user like:
    ~ Ben, 2 points, 4 tacos left
When we make a user, they start with the name we want and appropriate default values.
"""
# class HeyTaco():
#     def __init__(self, name="", tacos_to_give=5, score=0):
#         self.user_name = name
#         self.tacos_to_give = tacos_to_give
#         self.score = score
#     def __str__(self):
#         return "{}, {} points, {} tacos left".format(self.user_name, self.score, self.tacos_to_give)
#     def give_taco(self, number_given, other):
#         if self.tacos_to_give >= number_given:
#             self.tacos_to_give -= number_given
#             other.score += number_given
#             return True
#         else:
#             return False
# user1 = HeyTaco("Marnie")
# print(user1)
# user2 = HeyTaco("Marcus")
# user1.give_taco(2, user2)
# print(user1)
# print(user2)

"""
DO THIS NOW #12
Write a function to take in a filename and return the longest line of the file.
It should return a tuple of both line number and length in characters
"""
# def get_longest_line(filename):
#     length_longest_line = 0
#     line_count = 0
#     in_file = open(filename)
#     for line in in_file:
#         line_count += 1
#         if len(line) > length_longest_line:
#             length_longest_line = len(line)
#             longest_line = [line_count, length_longest_line]
#     return longest_line
# print(get_longest_line("text_example.txt"))

"""
DO THIS NOW #13
Write a program to determine which is the largest file in the current directory,
as defined by the total number of characters in the file.
You will need to use the os module
"""
# import os
#
# largest_filename = ""
# largest_number_of_characters = 0
# for filename in os.listdir("."):
#     with open(filename) as f:
#         length = len(f.read())
#         if length > largest_number_of_characters:
#             largest_filename = filename
#             largest_number_of_characters = length
# print(largest_filename)

"""
DO IT NOW #14
Write a recursive function that takes an integer and prints the numbers from it down to 0."""
# def countdown(number):
#     if number <= 0:
#         print(0)
#     else:
#         print(number)
#         countdown(number - 1)
# countdown(5)

"""
DO IT NOW #15
Write a program that swaps the content of a file "switch.txt" between "out" and "in" everytime is runs.
"""
# with open("switch.txt") as f:
#     file_content = f.read()
#     if "out" in file_content:
#         new_text = "in"
#     else:
#         new_text = "out"
# with open("switch.txt", 'w') as f:
#     f.write(new_text)