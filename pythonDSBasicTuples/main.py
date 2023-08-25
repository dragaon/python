# This is basic program to start with data science.
# Example program to deal with tuples, set operations and frozen sets
# In Tuples we can have tuple as a key as well. We can use any data structure that is
# immutable as a key

"""Tuples are ordered elements and immutable
Index start at 0 when you navigate from left to right
Index start at -1 when you navigate from right to left
"""
order_tuple = (1001, "10-Jan-23", 2900, "$", "user1")
# Nested Tuples
order_items_tuple = (1001, "user1", ("OrderItemId", "ProductId", "Price", "Quantity"),
                    (100101,198, 23.56, 2), (100102,1872, 1223.56, 1))

print(f"Order Date {order_tuple[1]}")
print(f"Order amount, currency and user is {order_tuple[2:5]}")

print (f"2nd element Order Items  is {order_items_tuple[1]}")
print (f"2nd Order Item price is  {order_items_tuple[2][2]}")
print (f"Rest of the Order Item details are {order_items_tuple[3:5]}")

shipment_order = order_items_tuple[::]

print(f"Cloned order item tuples are {shipment_order}")

#[] - List, () - tuple , {} Dictionary or Set
college_courses_set = {"Diploma", "Graduation", "Post Graduation", "PHD"}
school_courses_set ={"Nursery" , "Pre Primary", "Primary", "High School"}
specialization_courses_set = {"Mathematics" , "Science", "Social", "Statistics"}
print(f"Set type {type(college_courses_set)}")
union = college_courses_set|school_courses_set|specialization_courses_set
print(f"All courses - Union - {union}")
print(f"Common courses - Intersection - {union&school_courses_set}")

busNumbers = [10, 20, 34, 56]
frozenRoutes = frozenset(busNumbers)
busNumbers.append([56,26])
