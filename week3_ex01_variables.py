# Question 1: Variable Assignment and String Manipulation

# Ask the user for their name
name = input("Enter your name: Kiara Borens")

# Ask the user for their age
age = int(input("Enter your age: 18 "))

# Print a greeting
print(f"Hello {Kiara Borens}, you are {18} years old!")


#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# Ask the user for length
length = int(input("Enter the length of the rectangle:4 cm "))

# Ask the user for width
width = int(input("Enter the width of the rectangle:8 cm "))

# Calculate area
area = length * width

# Print result
print(f"The area of the rectangle is: {26cm}")


#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# Ask for temperature in Celsius
celsius = float(input("Enter temperature in Celsius:15 "))

# Convert to Fahrenheit
fahrenheit = (15 * 9/5) + 32

# Print rounded result
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


#------------------------------------------------------------------------------------
# If/Else Examples

# Example 1
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative number or zero")


# Example 2 (elif)
height = 175
if height < 150:
    print("Short")
elif height < 180:
    print("Average height")
else:
    print("Tall")


# Example 3 (nested if)
age_check = 25
if age_check >= 18:
    if age_check < 65:
        print("Adult")
    else:
        print("Senior")
else:
    print("Minor")