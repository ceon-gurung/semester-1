import random

# Read names from a file

with open("week1.8/session1/task1-random/names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
number = int(input("Enter a number "))

# Display the chosen names, one per line
chosen_names = random.sample(names, k=number)
print(chosen_names)