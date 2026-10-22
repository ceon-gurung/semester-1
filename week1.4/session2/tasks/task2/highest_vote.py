# Week 4, Session 2: Task 2
print()
def most_frequent_string(votes):
    if len(votes) == 0:
            return (None, None)
    """
    This function identifies the string that appears most frequently
    (highest count) in the votes argument and returns it along with the count
    of its occurrences. It assumes there is a single most frequent string
    (i.e., no ties for the highest count)

    Args:
        votes (list): A list of strings representng votes,
        e.g. ['apples', 'bananas', 'grapes', 'tomatoes']

    Returns:
        - tuple: (str, int) where str is the string with the highest count,
        and int is the count of its occurences
        - None, None: if votes is empty.
    """
    items = []

    new = True
    for voteItem in votes:
        new = True
        for i in range(len(items)):
            if items[i][0] == voteItem:                # if a vote entry exists
                items[i][1] += 1
                new = False

        if new == True:                         # if a vote entry doesn't exist, create vote entry
            items.append([voteItem, 1])         # voteItem, 1 vote (list, because tuples don't support item assignment)

    # convert list of lists into list of tuples
    items2 = []
    for list in items:
        items2.append((list[0], list[1]))

    favorite_voteItem = ("None", 0)
    for voteItem in items2:                          # find most voted item
        if voteItem[1] > favorite_voteItem[1]:
            favorite_voteItem = voteItem

    return favorite_voteItem

    # Your task is to complete the body of the function based on the details in the docstring.
    # Hint 1: You can complete this task with for loops or comprehensions 
    # Hint 2: Think about the properties of the various collection-types


fruit = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
         'date', 'elderberry', 'elderberry', 'date', 'banana']
names = ['Jesy', 'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jade',
         'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jesy', 'Jade',
         'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne',
         'Leigh-Anne', 'Jade', 'Jesy', 'Jade', 'Perrie', 'Jade',
         'Jade', 'Jesy', 'Perrie', 'Perrie', 'Jade', 'Leigh-Anne',
         'Jesy', 'Jesy', 'Perrie', 'Jesy']


# Check if correct output is produced
print(most_frequent_string(fruit))          # ('date', 4)
print(most_frequent_string(names))     # ('Leigh-Anne', 10)
print(most_frequent_string([]))             # (None, None)

# If completed, you could update the function to return all items that tie for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# tie, return a single string and a value as usual, e.g ('apples, 9).
