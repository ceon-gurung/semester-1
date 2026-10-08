# Worksheet 1.2: Task 1 Solution
import sys

valid = 0

try:
    gradeNumber = int(input("Enter a grade"))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if (gradeNumber >= 0) and (gradeNumber < 40):
    print(str(gradeNumber) + " is a Fail")
elif (gradeNumber >= 40) and (gradeNumber < 70):
    print(str(gradeNumber) + " is a Pass")
elif (gradeNumber >= 70) and (gradeNumber < 101):
    print(str(gradeNumber) + " is a Distinction")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")