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
