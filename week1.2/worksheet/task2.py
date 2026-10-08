# Worksheet 1.2: Task 2 Solution
"""
Utility functions for Worksheet 1.2.
"""

import sys

def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    if line == "":
        sys.exit("Error: no numbers provided")
    numbers = [float(item) for item in line.split()]
    return numbers

number = read_numbers()

print("Minimum = " + str(min(number)))
print("Maximum = " + str(max(number)))
print("Mean = " + str(sum(number)/len(number)))

number.sort()
if (len(number)%2 == 0):
    print("Median = " + str(((number[len(number)//2] + (number[(len(number)//2)-1]) ))/2))
else:
    print("Median = " + str(number[len(number)//2]))