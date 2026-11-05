# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        '''
        Creates a new person object with checked name and birth
        '''
        if name == "":
            raise ValueError("Name is empty")

        if not isinstance(name, str):
            raise TypeError("Name is not a string")

        birthTemp = birth.split('-')
        try:
            self.birth = date(int(birthTemp[0]), int(birthTemp[1]), int(birthTemp[2]))
        except:
            raise TypeError("birth must be a date object")
        
        self.name = name


    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        '''
        Returns the first letter of each name, capitalized
        '''
        initial = ""
        for char in self.name.split():
            initial += char[0].upper()
        return initial

    def is_birthday(self):
        '''
        Checks if a person's birthday is today
        '''
        if self.birth.month == date.today().month and self.birth.day == date.today().day:
            return True
        else:
            return False