
my_dict= {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA"
}
print(my_dict["name"])

print(my_dict.get("age"))

my_dict["age"] = 31
print(my_dict)

del my_dict["city"]
print(my_dict)

my_dict.clear()
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

if "name" in my_dict:
    print("Name is in the dictionary.")

my_dict.update({"name": "Alice", "age": 25})
print(my_dict)

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

print(students["alice"]["grade"]) 
print(students["bob"])