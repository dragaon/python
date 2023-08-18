# List, Sets and For loop data type
from helper import  validateInput, user_message
# List data type. Ordered sequence
employees_list = [10, "Prakash", "20-01-2934"]
print(f"Employee type is {type(employees_list)} and the length is {len(employees_list)}")
for employee in employees_list:
    print(str(type(employee)) + " " + str(employee))

employees_list.extend([7000000, 289847759])
print(f"Employee type is {type(employees_list)} and the length after adding element is {len(employees_list)}")

# Cloning employees list
employees_clone = employees_list[::]

user_input = input(user_message)
for eachValue in user_input.split(","):
    print(validateInput(eachValue))

print(employees_list[2])
employees_list.append("Narasapuram")
print(employees_list)
employees_list.remove(10)

#Set data type
set_of_employees = set(user_input.split(","))
print(f"Set data type is  {type(set_of_employees)}")
for eachEmployee in set_of_employees:
    print(validateInput(eachEmployee))

#Set data type
employees_set = {10, "Prakash", "30-Jul-1978"}
for eachEmployee in employees_set:
    print(eachEmployee)

employees_set.add("Chennai")
employees_set.add("Chennai")

print(employees_set)
employees_set.remove(10)
print(employees_set)
