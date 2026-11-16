# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    '''
    Test if the Money constructor can detect invalid "pounds" input
    '''
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    '''
    Test if the Money constructor can detect invalid "pounds" input
    '''
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    '''
    Test if the Money constructor can detect invalid input type
    '''
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:                       # There are multiple different types of errors. Raising TypeError
        m1 + 42                                                     # will make TypeError messages storeable as excinfo
    assert str(excinfo.value) == "other object must be a Money"


def test_invalid_type_pence():
    '''
    Test if the Money constructor can detect invalid "pence" input
    '''
    # complete the test implementation for 
    # invalid type for pence
    with pytest.raises(TypeError) as err:
        m2 = Money(0, "asd")
        assert(str(err.value)) == "pence must be an integer"
    

def test_invalid_value_pence():
    '''
    Test if the Money constructor can detect invalid "pence" input
    '''
    # complete the test implementation for 
    # invalid value for pence
    with pytest.raises(TypeError) as err:
        m3 = Money(0, -1)
        assert(str(err.value)) == "pence must be in range 0-99"

def test_valid_add():
    '''
    Test if the Money constructor can detect invalid Money addition
    '''
    # complete the test implementation for
    # valid add between money objects
    # Hint: you can compare using the __str()__ (
    # e.g., str(m1 + m2) == "£2.04"
    m4 = Money(1, 50)
    m5 = Money(2, 50)
    assert m4 + m5 == 4.00
    with pytest.raises(TypeError) as err:
            m3 = Money(0, -1)
            assert(str(err.value)) == "other object must be a Money"

test_invalid_type_pound()
test_invalid_value_pound()
test_add_invalid_type()
test_invalid_type_pence()
test_invalid_value_pence()
test_valid_add()