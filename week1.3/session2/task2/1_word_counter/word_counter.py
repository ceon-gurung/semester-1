# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

filename = "/workspaces/semester-1/week1.3/session2/task2/1_word_counter/story2.txt"

wordcount = 0

try:
    with open(filename) as f:
        contents = f.readlines()
        for line in contents:
            words = line.split()
            wordcount += len(words)
except:
    print(f"Error: the file {filename} could not be opened")

print(wordcount)

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210