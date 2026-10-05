# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {"album":"artist", "idk":"I don't look at album names much", "+":"Ed Sheeran", "-":"Ed Sheeran"}

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
print(music.get("album"))