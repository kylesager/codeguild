# filename: calculator.py
# learning objective: if/elif/else statements

# MVP - most viable product
# print welcome msg - d
# allow the user to enter two numbers - d
# allow the computer to randomly choose an operator
# print results using a conditional statement

# Stretch
# allow to pay again
# keep track of their "score"

import random
print(("*"*10) + "Welcome to the Gambling Calculator Game" + ("*"*10))
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

print(f"Your numbers: {num1} & {num2}")

operators_list = ["+", "-", "*", "/"]

chosen_operator = random.choice(operators_list)

print(chosen_operator)


# if/else = 2 conditions
# elif = more than 2 conditions

if chosen_operator == "+":
    results = num1 + num2
elif chosen_operator == "-":
    results = num1 - num2
elif chosen_operator == "*":
    results = num1 * num2
else:
    results = num1 / num2

print(results)
