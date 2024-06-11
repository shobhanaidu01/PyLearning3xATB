# 1. Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq - 4, c = 8

num = 2
square = num ** 2
cube = num ** 3

print(f"Square of {num} is: {square}")
print(f"Cube of {num} is: {cube}")


# 2. Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

#Inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is grater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equals to {num2}")
