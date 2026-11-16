# Week 1.7, Session 2: Task 1 - NameError

# Run this program and observe what happens

expenses = [10, 20, 30]

total = 0

for amount in expenses:
    total = total + amount              # total is created in the for loop, so it doesn't exist outside the for loop

print(total)