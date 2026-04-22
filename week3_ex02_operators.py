# Question 1
x, y = 10, 5
x += 3
y *= 2
print("Q1 Result:", x / y)


# Question 2
a, b, c = 15, 4, 10
final_condition = (a > b) or (b % 2 == 0 and c <= a)
print("Q2 Result:", final_condition)


# Question 3
score = int(input("Enter score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Question 4
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operation (+ - * /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/" and num2 != 0:
    print("Result:", num1 / num2)
elif op == "/" and num2 == 0:
    print("Cannot divide by zero")
else:
    print("Invalid operation")# Question 1
x, y = 10, 5
x += 3
y *= 2
print("Q1 Result:", x / y)


# Question 2
a, b, c = 15, 4, 10
final_condition = (a > b) or (b % 2 == 0 and c <= a)
print("Q2 Result:", final_condition)


# Question 3
score = int(input("Enter score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Question 4
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operation (+ - * /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/" and num2 != 0:
    print("Result:", num1 / num2)
elif op == "/" and num2 == 0:
    print("Cannot divide by zero")
else:
    print("Invalid operation")