"""
array_split():  Single Array to Multiple by Breaking
 along with adjusting no. of elements within each array
 if number of elements is less than required.

but

split()-method splits array without adjusting in each array
"""

# for example:
import numpy as np
single_arr = [12, 14, 56, 37, 86, 31]
print("The Original Array is:", single_arr)
splitted_array = np.array_split(single_arr, 3)
print("Splitting into 3 part of an Array:", splitted_array)

print("Accessing Required Partitioned Array: ")
print("1st Array-part:", splitted_array[0])
print("2nd Array-part:", splitted_array[1])
print("3rd Array-part:", splitted_array[2])

# Split 2-D arrays to 2-D Array:
unsplited_2D = np.array([[14, 47, 17], [25, 28, 58], [36, 39, 69],
                         [15, 19, 59], [26, 48, 36], [35, 37, 57]])
print("The Original 2D Array is:\n", unsplited_2D)
splited_2D = np.array_split(unsplited_2D, 2)
print("Splitting 2D to 2 elements as 2D:\n", splited_2D)

# split along the rows(axis=1): custom elemnt's-size splitting:
splited_2D_rows = np.array_split(unsplited_2D, 3, axis=1)
print("Split along Rows(axis-1): ", splited_2D_rows)

# hsplit()[opposite of hstack()]:
hsplited_2D_rows = np.hsplit(unsplited_2D, 3)
print("hSplit : ", hsplited_2D_rows)

# vsplit()[alternate of vstake()]:
# vertically n-array-split according to required no. of division
vsplited_2D_rows = np.vsplit(unsplited_2D, 3)
print("vsplit : ", vsplited_2D_rows)

# dsplit(): [alternate of dstake()] but works for 3D array to split the array:
