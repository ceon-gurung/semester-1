"""
    This task assumes some experience with Python.

    You are given incomplete function valid_char_in_string with a docstring.
    Your task is to complete the function based on the details in the
    docstring.
"""


def valid_char_in_string(popList, charSet):
    """
    This function takes two arguments popList and charSet, in which popList
    is a list of strings and charSet is a list of strings with a length of 1
    (a character).

    This function returns a Boolean False if any string in popList contains
    characters not in charSet, or invalid charSet. Otherwise, returns
    a Boolean True. Examples of valid charSet are ['0', '1'], ['-', '*'].
    """
    if type(charSet) != list:
        if len(charSet) > 1: # if not a single character
            return False

    for char in charSet:
        if len(char) > 1: # if not a single character
            return False

    for string in popList: # for each string in popList
        for popChar in string: # for each character in the string
            
            flag = False # checks if there is a match between popChar and setChar 3 lines down
            for setChar in charSet: # go through each character in charSet
                if popChar == setChar: # if the string and charSet characters match
                    flag = True
            if not flag: # if the flag is still false (no matches found)
                return False

    return True

# test data

plist1 = ['00000', '00001', '00010', '00011', '00100']
charset1 = ['0', '1']
print(valid_char_in_string(plist1, charset1))  # True

plist2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
          'ccg', 'cca', 'ata']
charset2 = ['a', 'c', 't', 'g']
print(valid_char_in_string(plist2, charset2))  # True

plist3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
charset3 = ['a', 'c']
print(valid_char_in_string(plist3, charset3))  # False

plist4 = ['00000', '00001', '00010', '00011', '00100']
charset4 = '01'
print(valid_char_in_string(plist4, charset4))  # False
