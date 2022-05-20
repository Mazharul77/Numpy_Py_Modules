"""
[ Bhuiyan-Note: Numerical Array(NumPy) as the py-library
 is used to working with array and array-operations/functionalities
 (several data sets creation, plotting, matrices, linear algebra, fourier transform, etc)
]
"""
# let's create any array & higher dimensional array with argument: ndim
import numpy as np  # aliasing numpy as np

# 1D - Array
my_arr1 = np.array(["Bhuiyan", 1425, "Mazharul", 1011])

print("My array is:", my_arr1)
print("The Type of the array is:", type(my_arr1))  # ndarray: array object type
print("The Size of my array:", len(my_arr1))
print("\n\t------ Here the Version of numpy -------:", np.__version__)

# 2D - Array (1D array as elements)
# but each matrix should have equal no. of attributes/values, same lengths
# sub module towards matrix : numpy.mat
my_arr2 = np.array([["software", 1, "engineer", 2], [11, 33, 55, 77]])

# 3D - Array (2D array as elements) :
# but each matrix should have equal no. of attributes/values(), same lengths
# sub module towards matrix : numpy.mat
my_arr3 = np.array([[["software", 1, "engineer", 2], [11, 100, 111, 1]],
                    [[11, 33, 55, 77], ["5A", 6876, "2C", -1]]])

# ndim attribute: Let's check whether check how many dimensions the array containing:
print("The my_arr2 Dimension is a:", my_arr2.ndim, end="-D Array\n")
print("The my_arr3 is a:", my_arr3.ndim, end="-D Array")
print("\n\tGiven 3D Array is:\n", my_arr3)
print("\n\t In my_arr3 First Array's 2nd Elementary-array(also array): ", my_arr3[0][1])
print("\n\t In my_arr3 First Array's 2nd Elementary-array(also array)'s 3rd element: ", my_arr3[0][1][2])


# 'ndmin' - argument:  Let's create Higher n dimensional Array with
any_dim_array = np.array([97, 88, 82, 91, ], ndmin=4)

print(any_dim_array)
print('-----------number of dimensions :', any_dim_array.ndim)
