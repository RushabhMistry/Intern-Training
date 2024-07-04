# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)  
print(fruits[0])  # apple
# Lists are mutable
fruits[0] = "blueberry"  # Modifying the first element
print(fruits)  # ['blueberry', 'banana', 'cherry']
fruits.append("date")  # Adding a new element
print(fruits)  # ['blueberry', 'banana', 'cherry', 'date']

# Tuples
coordinates = (10, 20)
print(coordinates[0])  # 10
# Tuples are immutable
# coordinates[0] = 30  # This will raise a TypeError: 'tuple' object does not support item assignment
print(coordinates)  # (10, 20)

# Sets
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}
# Sets are mutable but elements are unique
unique_numbers.add(5)  # Adding a new element
print(unique_numbers)  # {1, 2, 3, 4, 5}
# unique_numbers[0] = 6  # This will raise a TypeError: 'set' object does not support indexing

# Dictionaries
student = {"name": "Alice", "age": 25}
print(student["name"])  # Alice
# Dictionaries are mutable
student["name"] = "Bob"  # Modifying the value for the key 'name'
print(student)  # {'name': 'Bob', 'age': 25}
student["grade"] = "A"  # Adding a new key-value pair
print(student)  # {'name': 'Bob', 'age': 25, 'grade': 'A'}
