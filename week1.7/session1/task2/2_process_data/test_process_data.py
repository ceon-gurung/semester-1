# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    '''
    Test if process_data([]) returns None
    '''
    assert process_data([]) == None
    # complete the implementation for
    # testing an empty list
    
    
def test_one_int_list():
    '''
        Test if process_data([1]) returns 1
        '''
    assert process_data([1]) == 1
    # complete the implementation for 
    # testing a list with a single integer


def test_multiple_int_list():
    '''
        Test if process_data([1, 2, 3]) returns 6
        '''
    assert process_data([1, 2, 3]) == 6
    # complete the implementation for
    # testing a list with multiple integers

test_empty_list()
test_one_int_list()
test_multiple_int_list()