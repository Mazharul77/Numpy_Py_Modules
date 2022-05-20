# ..........Shape & Reshape: Let's implement here: ..........
"""shape: In each dimension No. of element:
 returns a tuple with each index having the number of corresponding elements"""
import numpy as np

# shape of 3D array:
arr = np.array([[[1, 2, 3, 4], [5, 2, 3, 4], [6, 2, 3, 4]],
                [[7, 2, 3, 4], [8, 2, 3, 4], [9, 2, 3, 4]]], ndmin=3)
# (2,3,4) : 2(Two) 3D(three dimensional) Arrays where each array has 4 elements/values

print("The Given Array:", arr)
print("Shape of arr :", arr.shape)


# 2D array shape:
arr_2d = np.array([['a', 'p', 'p', 's'], ['d', 'e', 'v', 'e']])
print("The arr_2d", arr_2d)
print("The shape of arr_2d", arr_2d.shape)
# (2,4) : the array has 2-dimensions
# whereas first dimension has 2 elements(['a', 'p', 'p', 's'], ['d', 'e', 'v', 'e'])
# and the second dimension has 4 elements each([a, p, p, s] or [d, e, v, s])

# ndmin: array creation
print("Lets create n-dimensions(with ndmin) using a vector along the values:")
m_array = np.array(['M', 'a', 'z', 'h', 'a', 'r', 'u', 'l'], ndmin=4)
print("The m_array:", m_array)
print("The shape of created m_array:", m_array.shape)
# (1, 1, 1, 8) : Here in the above the last dimension(at 3rd index as 4D) has 8 values

print("\n\t ......Reshaping(adding/removing dimensions): Changing Array shape:.......")
print("Conversion of 1D(with 8 elements)  to 2D(4 arr with 2 elements): ")
m_array_1d = np.array(['M', 'a', 'z', 'h', 'a', 'r', 'u', 'l'])
m_array_1d_new = m_array_1d.reshape(4, 2)
print("The Converted 1d to 2d m_array_1d_new:\n", m_array_1d_new)

#
print("Conversion of 1D(with 12 elements)  to 3D(2 arr containing 2 arrays, each with 5 elements): ")
m_array_1d_ = np.array(['M', 'a', 'z', 'h', 'a', 'r', 'u', 'l',
                       'I', 's', 'l', 'a', 'm',
                       'B', 'h', 'u', 'i', 'y', 'a', 'n'])
m_array_1d_n3dew = m_array_1d_.reshape(2, 2, 5)
print("The Converted 1d to 2d m_array_1d_new:\n", m_array_1d_n3dew)

# Let's check whether returned array is a copy or a view:
# if view then return the original array
# otherwise it's copy & it'll return: none
print("The Base of the reshaped m_array_1d_n3dew:", m_array_1d_n3dew.base)


print("\n\tLet's Automate Array Automation to unknown dimensional array reshaping:")
"""[It's noted that we can't use/pass:-1
 as element's value for more than 1D array]"""

# unknown dimension(passing -1 as value) in numpy : auto calculated each elements to conversion
# we don't need to specify the exact dimension to reshape
arr_rand = np.array([1, 2, 3, 4, 5, 6, 7, 8])

arr_auto = arr_rand.reshape(1, 2, -1)
print("The Automated Converted reshaped array from:\n", arr_rand, "to\n", arr_auto)

# another one
arr_3d = np.array([[[1, 2, 3, 4, 11, 13]], [[12, 5, 6, 7, 8, 14]]])

arr_3d_auto = arr_3d.reshape(1, 3, -1)
print("The Automated Converted reshaped array from:\n ", arr_3d_auto)


# Array Flattening from multidimensional to 1D: reshape(-1)
print("\n\tMultidimensional to 1D using reshape(-1):\n ", arr_3d.reshape(-1))

