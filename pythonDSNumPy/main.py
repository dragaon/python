# This is a sample Python code for numpy.
import random

import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

distance = [10.9,23.4,56]
time=[1,3,5]

np_distance = np.array(distance)
np_time = np.array(time)
speed = np_distance/np_time

print(f"Speed is {speed} and the shape is {np.shape(speed)}")

student_marks = (10,34,56,78)
print(f"Multiplying tuple {student_marks} with 3 results repeating "
      f"elements in a tuple three times {student_marks * 3}")
print(f"Multiplying tuple {student_marks} with 3 by converting into numpy array "
      f" {np.array(student_marks) * 3}")

zero_dim_arr = np.array(10)
one_dim_arr = np.array([10,23,56,22])
print(f"Dimension of array {zero_dim_arr} is {zero_dim_arr.ndim} and {one_dim_arr} is {one_dim_arr.ndim}")
multi_dim_arr = np.array(
    [[[1,2],
     [3,4]
    ],
    [[5,6],
     [7,8]
    ],
    [[9,10],
     [11,12]
    ]]
)

print(f"Multi Dimension of array is {multi_dim_arr.ndim} and size is {multi_dim_arr.size} "
      f"and shape is {multi_dim_arr.shape}")

multi_dim_arr1 = np.array([
    [1,2,3],
    [4,5,6]
])
print(f"Multi Dimension of array1 {multi_dim_arr1} "
      f"dimension  is {multi_dim_arr1.ndim} and size is {multi_dim_arr1.size} "
      f"and shape is {multi_dim_arr1.shape} ")

multi_dim_arr1.shape = (3,2)
print(f"Multi Dimension of array1 after reshaping to 3 ,2 is "
      f"{multi_dim_arr1}")

single_dim_arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
multi_dim_arr_reshape = single_dim_arr.reshape(3,5)
print(f"Single Dimension of array {single_dim_arr} after reshaping to 3 ,5 is "
      f"{multi_dim_arr_reshape}")

print(f"First element in each array from multi_dim_arr_reshape {multi_dim_arr_reshape[:,0]}")
print(f"2nd and 3rd element in each array from multi_dim_arr_reshape {multi_dim_arr_reshape[:,(1,2)]}")

#Slicing of array with Start and end
print(f"Slicing 0 to 3 elements in array {single_dim_arr} is {single_dim_arr[0:3]}")
#Slicing of array with Start, end and step
print(f"Slicing Elements in array with step 2 {single_dim_arr} is {single_dim_arr[0:154:2]}")

#Two dimensional slicing
slice_md_array = np.array([
    [1,2,3,4,5,6],
    [11,12,13,14,15,16],
    [21,22,23,24,25,26]
])
print(f"Slicing multi dimensional Elements in array 2,1,4  {slice_md_array} is {slice_md_array[:2,1:4]}")
print(f"Slicing multi dimensional Elements in array  2,2 {slice_md_array} is {slice_md_array[:2,2]}")

print(f"Mean of the multi dimensional array is {np.mean(slice_md_array)} and "
      f"Median is {np.median(slice_md_array)}  and "
      f"Average is {np.average(slice_md_array)}")

#Stacking array
apac_country_ranks = np.array([10,2,34,5])
emea_country_ranks = np.array([33,54,12,78])
nam_country_ranks = np.array([331,534,132,7])
print(f"Stracking array of apac, emea and nam is "
      f"{np.hstack((apac_country_ranks, emea_country_ranks,nam_country_ranks))}")


#Randomly generate number
print(f"Generating 12 random consecutive integer values {np.arange(12)}")
print(f"Generating random values using linspace {np.linspace(2,3,12)}")

random_array = np.random.random(10)
print(f"Generating random numbers using random {random_array} and dimension is "
      f"{random_array.ndim} and the size is {random_array.size} and "
      f"shape is {random_array.shape}")

random_array1 = np.random.randn(3,3)
print(f"Generating random numbers using random {random_array1} and dimension is "
      f"{random_array.ndim} and the size is {random_array1.size} and "
      f"shape is {random_array1.shape}")

print(f"Generating random number within a range {np.random.randint(5,29)}")
random_array2 = np.random.randint(1,20,(3,3))
print(f"Generating random numbers using random {random_array2} and dimension is "
      f"{random_array.ndim} and the size is {random_array2.size} and "
      f"shape is {random_array2.shape}")

#Fixing the random ness
for i in range(5):
    random.seed(20)
    print(f"Generating random int after seed is {random.randint(4,90)}")

#ravel converts multidimensional array to single dimensional arry
ravel_demo = np.random.randint(1,10,(2,3,4))
print(f"Array with 3 X 4 is {ravel_demo} and after using ravel is {np.ravel(ravel_demo)}")

flatten_demo = np.array([[1,2,3],[11,12,13],[21,22,23]])
print(f"Array with 3 X 3 is {flatten_demo} and after using flatten is "
      f"{np.ndarray.flatten(flatten_demo, order='C')}")
print(f"Array with 3 X 3 is {flatten_demo} and after using flatten is "
      f"{np.ndarray.flatten(flatten_demo, order='F')}")

print(f"Generating elements using Arrange {np.arange(2,4,.5)}\n "
      f"and type is {type(np.arange(2,4,.5))}")