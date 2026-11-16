import random

# Get user to input how many random numbers they want
amount = int(input("How many random numbers do you want? "))

# Generate this many random numbers
nums = [random.random() for i in range(amount)]

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", 'x') as f:
    for i in nums:
        # add each number
        f.write(str(i) + "\n")