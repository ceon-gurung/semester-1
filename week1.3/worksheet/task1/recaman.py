# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]
integer = 0
unique = False

for i in range (1,L+1):
    unique = True
    integer = sequence[i-1]

    # Find duplicates
    for num in sequence: # go through every number in sequence
        if ((integer - i) == num) and (unique):    # if new number is not in list
            unique = False                        # then show that it's unique and quit
    
    if ((integer - i) > 0) and unique:                                # ak-1 – k > 0
        sequence.append(integer - i)
    else:
        sequence.append(integer + i)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence