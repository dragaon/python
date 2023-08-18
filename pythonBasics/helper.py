# Reusable functions which can be used and imported by other python programs
def days_to_units(num_days, units):
    if num_days > 0:
        result = num_days * 60 * 60
        return f"In function Hours {result} {units}"
    elif num_days == 0:
        return "Please enter positive number > 0"
    else:
        return "Please enter positive number"


def add(a, b):
    try:
        c = int(a) + b
        print(f"Add function result {c}")
        return c

    except:
        print("Invalid input. Please enter numeric numbers only")
        return 0


def validateInput(inputValue):
    try:
        int(inputValue)
        return f"Entered input value {inputValue} is an integer"
    except:
        return f"Entered input value {inputValue} is not an integer"


user_message = "Please enter the list\n"
