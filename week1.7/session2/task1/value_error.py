# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

for key, value in user_profile.keys(), user_profile.values(): # user_profile only gave the keys.
	print(f"{key} : {value}")