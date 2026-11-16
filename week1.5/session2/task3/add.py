# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

class Money:
    def __init__(self, amount):
        '''
        Set this object's amount property
        '''
        self.amount = amount

    def __add__(self, other):
        '''
        Add together this object's amount property and another object's money property
        '''
        return self.amount + other.amount

a = Money(10)
b = Money(15)
print(a+b)