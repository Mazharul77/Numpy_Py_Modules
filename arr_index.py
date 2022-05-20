# This is array-indexing based concept in nummpy
"""Suppose we want to find out the middle point number of any sorted array...."""
import numpy as np
arr_ = np.array([22, 11, -55, 99, 98])
s_arr_ = np.sort(arr_)
print("The Given Array:", arr_)
print("The Sorted  Array:", s_arr_)
print("The Mid number of the sorted value is: %.0f" % ((s_arr_[0]+s_arr_[-1])/2))

# Let's create 2D Matrix Array:
arra_2d = np.array([[31, 31, 32, 39],
                    [42, 41, 43, 44]])

print("Dimension arra_2d:", arra_2d.ndim)
print("\n\t 2D-Array - Accessing  2nd row's(2nd array) -> 4th element :", arra_2d[1, 3])

# Let's create 3D Matrix Array:
arra_3d = np.array([[[11, 221, 112, 4],
                     [22, 21, 23, 24]],

                    [[31, 31, 32, 39],
                     [42, 41, 43, 44]]])
print("Dimension arra_3d:", arra_3d.ndim)
print("\n\t 3D-Array - Accessing 2nd row's(2nd array) -> 1st elementary row's(1st array) 3rd element:", arra_3d[1, 0, 2])