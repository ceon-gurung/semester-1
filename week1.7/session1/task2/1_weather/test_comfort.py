# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level
import unittest

def test_cold():
    '''
    Test if comfort_level returns "COLD"
    '''
    assert comfort_level(10) == "COLD"
    assert comfort_level(15) == "COLD"

def test_hot():
    '''
    Test if comfort_level returns "HOT"
    '''
    assert comfort_level(30) == "HOT"
    assert comfort_level(25.1) == "HOT"
    
test_cold()
test_hot()