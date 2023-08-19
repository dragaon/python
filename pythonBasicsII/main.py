# This is basic program to understand data science.
# Example program to deal with tuples

#Index start at 0
tuple_demo = (1, 10, 29, "Prakash", "Chennai", 10.34)
# Nested Tuples
nested_tuple_demo = ("CBSE", "10th Grade Marks", ("Name", "Maths", "Science", "Social"),
                    ("Student1", 99, 98, 99), ("Student2", 100, 98, 100), 90, 1092039, 299844, 38838)

print(f"Tuple value at element 3 is {tuple_demo[2]}")
print(f"Tuple range from element 3 is {tuple_demo[2:5]}")

print (f"Nested Tuple value at element 3 is {nested_tuple_demo[2]}")
print (f"Nested Tuple value at element 3 and element 1 is {nested_tuple_demo[2][0]}")
print (f"Tuple range from element 3 is {nested_tuple_demo[2:5]}")
