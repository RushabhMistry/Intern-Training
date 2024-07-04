# # Conditional statements
# age = 20
# if age < 18:
#     print("You are a minor.")
# elif 18 <= age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior.")

# # Loops
# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1
    
# _________________________________________________________________

# Conditional statements
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Loops
n = int(input("Enter the number of iterations for the for loop: "))
for i in range(n):
    print(i)

m = int(input("Enter the number of iterations for the while loop: "))
i = 0
while i < m:
    print(i)
    i += 1    