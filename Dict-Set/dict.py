new_dict = {
    "name": "Demo",
    "age": 25,
    "city": "Hyderabad",
    "city" : "Hyderabadi", # Duplicate key, will overwrite the previous value
    "marks": [85, 90, 95],
    "cgpa": 9.6,
}
print(new_dict)
# Accessing values using keys
print(new_dict["age"])
# Adding a new key-value pair
new_dict["Country"] = "India"
print(new_dict)

# Updating an existing key-value pair
new_dict["age"] = 26
print(new_dict)

# Removing a key-value pair
del new_dict["city"]
print(new_dict)

