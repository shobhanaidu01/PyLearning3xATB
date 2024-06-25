# ✅ Conditions
# age > 18 -> You are allowed to go the club
# age < 18 -> You are not allowed

# pramod -> goa -> father permission
# pramod -> no goa -> no permission

# If, ELSE
# Syntax
# if condition:
#     code to be executed
# else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# Take a user input

age = int(input("Enter your Age"))

if age > 18:
    print("Go to the club")
else:
    print("Not allowed")

age = int(input("Enter your age - "))

if age > 18:
    print("Go to the club")
else:
    print("Not allowed")

# Question: Write a Python program that asks the user for their age and prints different messages based on the age entered:

age = int(input("Enter your age - "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

number = int(input("Enter a number - "))

if number % 2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")