"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

for i in range(maxtime+1):
    if state == "red":
        for j in range(4):
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "amber"
    
    if state == "red_amber":
        for j in range(3):
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "green"
    
    if state == "green":
        for j in range(5):
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "amber"
    
    if state == "amber":
        for j in range(3):
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "red"

# At the end of each step you should output the time and state using the statement on line 14