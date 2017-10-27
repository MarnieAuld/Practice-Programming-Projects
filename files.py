"""
Files I/O Programming Practice
"""

"""
Write a GPA-calculating program that reads subject scores from a file. 
The program should print each score and the corresponding grade plus the final GPA at the end.
(GPA stands for Grade Point Average. You should aim to have a high one!)
"""


"""
Write a program that uses functions to do the following:
*** Use a menu to present the user with options 
*** Make a function for your menu that displays the menu text, 
    gets the user's choice and converts it to uppercase (and returns it).
Calculating a grade is based on the user's score and works like: <50 = N, 50-64 = P, 65-74 = C, 75-84 = D, >= 85 = HD.
(Floats should be handled, e.g. 74.95 is a C.)
*** Use a function that only calculates the grade, but does not display it.
*** Use a "dummy" function for calculateGPA. 
    So write a function definition that just prints "Your GPA is ...", but set up the main program so it calls this.
"""


"""
Add the calculateGPA facility to your grade program:
It should ask the user for each of their subject scores (raw numbers), 
    convert the score to a grade, convert the grade to a weight, then calculate the average of those.
Use a while loop to get their scores until they enter a negative value (that's the sentinel or stopping condition).
If we were able to use lists, we could store each score for later and our GPA function could accept a list, 
    but we will just calculate the total on the fly (like we did for average age last week), 
    so we need to keep track of the number of subjects.
Weights for GPA are: N = 1.5, P = 4, C = 5, D = 6, HD = 7
Think about what functions you need to write and what functions you can reuse.
Modify the above program so that the file also has subject codes - i.e. each line looks something like CP1404 86
"""


"""
Write a program that allows the user to find how many times a word appears in a file. 
They should enter the filename and a word, and it tells them how many times the word is in that file.
"""