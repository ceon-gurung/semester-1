# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["York"] = "Ouse"
rivers["London"] = "Severn"
# Display all the keys
for item in rivers:
    print(rivers.get(item))
# Display all the values
for item in rivers:
    print(item)
# Display all the key:value pairs, as tuples
print(rivers.items())
# Delete an entry from the rivers database
rivers.pop("Leeds")

print(rivers)