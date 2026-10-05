# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(fruit.index("banana"))
# Display how many times "cherry" occurs
count = 0
for item in fruit:
    if item == "cherry":
        count += 1
print("Cherry occurs " + str(count) + " times")
# Display how many times "strawberry" occurs
count = 0
for item in fruit:
    if item == "strawberry":
        count += 1
print("Strawberry occurs " + str(count) + " times")
# Unpack tuple into variables
a, b, c = fruit

print(a) # apple
print(b) # banana
print(c) # cherry