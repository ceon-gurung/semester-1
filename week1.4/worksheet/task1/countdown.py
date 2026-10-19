
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    
    print(number)
    if number != 0:
        countdown(number-1)