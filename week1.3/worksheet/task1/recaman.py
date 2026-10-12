# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]
integer = 0
unique = False

for i in range (1,L+1):
    unique = False
    integer = sequence[i-1] - i

    # Find duplicates
    for num in sequence: # go through every number in sequence
        if (integer != num) and not (unique):    # if new number is not in list
            unique = True                        # then show that it's unique and quit
            print(unique)
    
    if (integer > 0) and unique:                                # ak-1 – k > 0
        sequence.append(integer)
    else:
        sequence.append(sequence[i-1] + i)

    if unique:
        print("unique: " + str(sequence[len(sequence)-1]))

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence