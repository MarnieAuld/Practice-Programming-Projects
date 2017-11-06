"""
Strings Programming Practice
"""

"""
Write a program to calculate the number of uppercase and lowercase letters in a string
"""
# string = "This is an ExamPle String with Uppercase and LowerCase LeTters"
# upper_count = 0
# lower_count = 0
# total_count = 0
# for character in string:
#     total_count += 1
#     if character.isupper():
#         upper_count += 1
#     else:
#         lower_count += 1
# print("The string with {} characters in total has: \n{:3} Uppercase characters \n{:3} Lowercase characters"
#       .format(total_count, upper_count, lower_count))


"""
Prompt the user for an input and capitalize every second letter in the input
"""
user_string = input("Enter a string: ")
new_string = user_string[::2].upper()
print(new_string)