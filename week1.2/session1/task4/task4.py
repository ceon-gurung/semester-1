# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
# Remove an item from vegetables
vegetables.remove("leek")
# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))