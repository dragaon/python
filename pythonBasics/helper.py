# Reusable functions which can be used and imported by other python programs
import logging

#Global variable
user_message = "Please enter comma separated values to create a list\n"
logger = logging.getLogger("Helper")

#Multiline Commets can be written by enclosing comments in """
"""Function returns by converting number of days to the 
given units ie. minutes or seconds """
def days_to_units(num_days, units):
    if num_days > 0:
        match units:
            case "seconds":
                return num_days * 24 * 60 * 60
            case "minutes":
                return num_days * 24 * 60
            case default:
                logger.error(f"ERROR: Entered unit value {units} is not valid")
                return -1
    elif num_days == 0:
        return num_days
    else:
        logger.error(f"ERROR: Entered values {num_days} is not >0")
        return -1


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
        return bool(1)
    except:
        return bool(0)


def logMsgNewLine(message):
    print(f"{message} \n")
