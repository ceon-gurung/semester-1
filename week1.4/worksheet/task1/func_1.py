
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) # finds how many numbers there are
    for value in lst_value: # adds together all numbers
        sum = sum + value 
    return sum/num_of_value # returns mean