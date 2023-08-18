# Basic Python program for beginners. It contains basics with While Loop
import helper

print("Hello\nworld Python application")

print(bool(1))
a=5
print (f"Float division {6/2}")
print (f"Integer division {6//2}")
print (f"Value of a is {a}")
print("Value is ")
a = 10
print(a + 20)
print(a ^ 2)
print("Don't repeat value " + str(50) + " done")
# using numeric values to be displayed
print(f"Don't repeat value {50} done")
num_days = -10

calculation = 60 * 60
units = "minutes"
user_input = input("Please enter number to add")
if user_input.isdigit():
    user_input = int(user_input)
    print(helper.days_to_units(user_input, units))
else:
    print("User Validation failed. Please enter positive number > 0")
print(num_days)

user_input = ""

while "exit" != user_input:
    user_input = input("Please enter number to add\n")

    try:
        b = int(user_input) + 1
        c = helper.add(user_input, b)
        print(c)
    except:
        print("Invalid input. Please enter numeric numbers only")
