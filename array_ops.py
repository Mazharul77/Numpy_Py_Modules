# Array Iteration: Iteration on n-D array will go through as (n-1)th dimension one by  one
import numpy as np

# For 2D array:
arr_mat = np.array([[11, 22, 33, 44, 5], [12, 21, 51, 67, 99]])
print("Accessing elements one by one: ")

print("The 2D arrays are:\n")
for elem in arr_mat:
    print(elem)

print("\nThe Items in each inner Array_dim:\n")

for elem in arr_mat:
    c = 0
    for each_val in range(0, len(elem)):
        c = c + 1
        print(elem[each_val])
        if (len(elem)) == c:
            print("\n.........")
    print("\n\t=======")

# For 3D array:
arr_mat_3D = np.array([[[11, 22, 33, 44, 5]], [[12, 21, 51, 67, 99]]])
print("\n\tThe Type of arr_mat_3D:", arr_mat_3D.ndim)
print("Accessing Array as for 3D as 2D one by one:")
for part in arr_mat_3D:
    for inner_arr in part:
        for single_value in inner_arr:
            print(single_value)

# nditer() : high dimensional iteration with less loop to reduce complexity
# Let's see the difference:
print("\n\tHigh Dimensional Array Iteration with nditer():")
for it in np.nditer(arr_mat_3D):
    print(it)

# Without nditer() it'll return just the arrays as element:
print("\n\tArray Iteration without nditer():")
for it in arr_mat_3D:
    print(it)

# op_dtypes : iteration with data-types with extra buffered space in nditer():
# by passing flags = ['buffered']
print("The Array with custom expected data-types:")
for individual in np.nditer(arr_mat_3D, flags=['buffered'], op_dtypes=['S']):
    print(individual)

# n-step iteration: iteration with different step size:
# Filtering with iteration:
a_2d = np.array([[45, 231, 69, 487, 363], [121, 120, 789, 4, 5]])
print("\n\t Accessing the Values of Matrix(2D) Skipping 1 item(Even-index):")
for val in np.nditer(a_2d[:, ::2]):
    print(val)
#
a_3d = np.array([[[45, 231, 69, 487, 363]], [[121, 120, 789, 4, 5]]])
print("\n\t Accessing the Values of Matrix(3D) Skipping 1 item(Even-index):")
for val in np.nditer(a_3d[:, :, ::2]):
    print(val)


# ndenumerate(): sequence number of something like index of corresponding values/elements

# For 1D array index and value access:
a_1D = np.array([44, 55, 66])
print("\n\tThe 2D aArrays index with value with ndenumerate():")
for pos, term in np.ndenumerate(a_1D):
    print(pos, term)

""" Output For 1D (1D-enumeration:)
The 2D aArrays index with value with ndenumerate():
(0,) 44
(1,) 55
(2,) 66
"""
# For 2D array index and value access:
a_2D = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print("\n\tThe 2D aArrays index with value with ndenumerate():")
for id, elem in np.ndenumerate(a_2D):
    print(id, elem)

""" Output For 2D (2D-enumeration:)
The 2D aArrays index with value with ndenumerate():
(0, 0) 11
(0, 1) 22
(0, 2) 33
(1, 0) 44
(1, 1) 55
(1, 2) 66
(2, 0) 77
(2, 1) 88
(2, 2) 99
"""


# np.ndenumeration() of 3D array:

print("Index with Value of 3D-Arrays:")
for indx, value in np.ndenumerate(a_3d):
    print(indx, value)

""" The Output will look like:
Index with Value of Arrays:
(0, 0, 0) 45
(0, 0, 1) 231
(0, 0, 2) 69
(0, 0, 3) 487
(0, 0, 4) 363
(1, 0, 0) 121
(1, 0, 1) 120
(1, 0, 2) 789
(1, 0, 3) 4
(1, 0, 4) 5
"""