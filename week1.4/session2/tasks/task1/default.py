# Week 4, Session 2: Task 1

def greeting(name='John'):
    '''
    Returns the string "Good morning", followed by the input string.
    The input string defaults to "John"
    '''
    # Your task is change the default name to your name and observe the output
    print(f'Good morning {name}')


# Check if correct output is produced
greeting()

# write a second test by passing a name to the function

greeting("bob")