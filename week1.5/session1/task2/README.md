# Task 2

Try running `badclass1.py`. Examine the error message carefully.

What is the specific cause of this error? What should we change in the
definition of `Point` to fix it?

    add "self" to the start of the __init__() parameters

Now try running `badclass2.py`. This demonstrates a different problem.
Again, examine the error message carefully.

What is the specific cause of this error? What should we change to fix it?

    the variable x was defined inside the Point object. the Point object p was not affected
    inside __init__(), replace x and y with self.x and self.y

Before applying any fixes to these problems, try running `pylint` on each
of these files by entering the following commands in the terminal:

    pylint badclass1.py
    pylint badclass2.py

(Make sure you are in the same directory as the files before doing this!)

This tool will report a number of issues, including the specific problems
that prevent the class definitions from working correctly.
