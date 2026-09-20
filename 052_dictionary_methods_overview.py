capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# Safe lookup using .get()
print(capitals.get("USA"))
print(capitals)

# Checking key existence safely
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital does not exist.")

# Add new pair and update existing pair
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
print(capitals)

# Remove specific key
capitals.pop("China")
print(capitals)

# Remove the last inserted item
capitals.popitem()
print(capitals)

# Get keys view and iterate
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# Get values view and iterate
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

# Get key-value pairs (items) and unpack in a loop
items = capitals.items()
print(items)

for country, capital in capitals.items():
    print(f"{country}: {capital}")

# Clear all entries from the dictionary
capitals.clear()

print(capitals)