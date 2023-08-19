# Basic Python program for beginners. Code contains
# 1. Print statement, Using If, While loop, user input
# 2. Defining function
# 3. Importing other python functions
# 4. Basic exception handling

import helper

print("Hello\nworld Python application")
print(bool(1))

a=5
print (f"Float division {6/2} Integer division {6//2}")
print (f"Value of a is {a}")
a = 10
print(f"{a + 20} and {a ^2} and type of a is {type(a)}")
print(a ^ 2)

# using numeric values to be displayed
print(f"Don't repeat value {50} done")
num_days = -10

calculation = 60 * 60
units = "minutes"
user_input = input(f"Please Enter number of days to convert to {units}:\n")
if user_input.isdigit():
    user_input = int(user_input)
    print(f"{user_input} day(s) = {helper.days_to_units(user_input, units)} {units}")
else:
    helper.logMsgNewLine("User Validation failed. Please enter positive number > 0")

user_input = ""

while bool(1):
    user_input = input("Please enter number to add\n")
    if "exit" == user_input:
        break
    try:
        b = int(user_input) + 1
        helper.logMsgNewLine(f"The sum of {user_input} and {b} is {helper.add(user_input, b)}")
    except:
        helper.logMsgNewLine("Invalid input. Please enter numeric numbers only")

helper.logMsgNewLine("Thank you for using the program. Best of luck!!!")