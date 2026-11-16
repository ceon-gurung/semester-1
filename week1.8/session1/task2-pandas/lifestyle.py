import pandas

data = pandas.read_csv("week1.8/session1/task2-pandas/lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print(type(data)) ## <class 'pandas.DataFrame'>

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
# 2000 (2001 lines - 1 line for header = 2000 entries)

# Find the mean average GPA of the students
print(data["GPA"].describe("mean"))

# Find the standard deviation of how much sleep students get per day
print(data.select("Sleep_Hours_Per_Day").describe("std"))

# Find the maximum amount of study hours per day
print(data[data["column"]=="Study_Hours_Per_Day"].describe("max"))

# Sort the students by social hours per day ascending (lowest -> highest)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
