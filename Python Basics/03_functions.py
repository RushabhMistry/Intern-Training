# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))

# def add(a, b):
#     return a + b

# print(add(3, 5))

# ______________________________________________________________

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Taking user input for the greet function
user_name = input("Enter your name: ")
print(greet(user_name))

# Taking user input for the add function
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(add(num1, num2))
