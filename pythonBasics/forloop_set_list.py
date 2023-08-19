# Sample code which contains usage of
# List, Sets and For loop
from helper import  validateInput, user_message

# List data type. Ordered sequence
employees_list = [10, "Python Programmer", "20-01-2934"]
print(f"Employee type is {type(employees_list)} and the "
      f"length is {len(employees_list)}")
for employee in employees_list:
    print(str(type(employee)) + " " + str(employee))

employees_list.extend([7000000, 289847759])
print(f"Employee type is {type(employees_list)} and the length after adding "
      f"element is {len(employees_list)}")

# Cloning employees list
employees_clone = employees_list[::]

user_input = input(user_message)
for eachValue in user_input.split(","):
    isInt = validateInput(eachValue)
    print(f"Is each entered value {eachValue} is integer? {isInt}")
    if bool(1) == isInt:
        employees_clone.append(eachValue)

print(f"2nd element in the employee list is {employees_list[2]}")
employees_list.append("Bangalore")
print(f"Elements in the employee list is after appending element : {employees_list}")
print(f"Elements in the employee clone list is after appending element in employee: {employees_clone}")

employees_list.remove(10)
print(f"Elements in the employee list is after removing element with value 10: {employees_list}")

#Set data type
set_of_employees = set(user_input.split(","))
print(f"Set data type is  {type(set_of_employees)}")

for eachEmployee in set_of_employees:
    print(f"Elements from Set is {eachEmployee} and type is {type(eachEmployee)}")

set_of_employees.add("Mumbai")
#Try adding duplicate value
set_of_employees.add("Mumbai")

print(f"Employee list after adding duplicate values : {set_of_employees}")
set_of_employees.remove(10)
print(f"Employee list after removing element value 10 : {set_of_employees}")
