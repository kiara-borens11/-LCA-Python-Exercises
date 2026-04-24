# ---------------- Question 1: Using a for loop with a list ----------------

# Create a list of fruits
fruits = ["apple", "banana", "orange", "grape"]

# Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)


# ---------------- Question 2: Using a while loop for countdown ----------------

# Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
    print(count)
    count -= 1


# ---------------- Question 3: Using a for loop with range() ----------------

# Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    print(i ** 2)


# ---------------- Question 4: Using the random module ----------------

# Import the random module
import random

# Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]

# Use a for loop to select and print 3 random colors from the list
for i in range(3):
    print(random.choice(colors))


# ---------------- Question 5: Creating and using a custom module ----------------

# NOTE:
# Create a separate file called math_operations.py and paste this inside it:

"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# Import the custom module
import math_operations

# Use a while loop to create a simple calculator
while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", math_operations.add(num1, num2))
    elif choice == "2":
        print("Result:", math_operations.subtract(num1, num2))
    elif choice == "3":
        print("Result:", math_operations.multiply(num1, num2))
    elif choice == "4":
        print("Result:", math_operations.divide(num1, num2))
    else:
        print("Invalid choice")