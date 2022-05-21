"""
Sorting Sequentially(alphabetical/numerical value) in Numpy array
Ascending or Descending order
"""
import numpy as np
unsorted_arr = np.array([8, 5, 77, 88, 33, 5, 98, 86])
str_array = np.array(['teacher', 'Varsity',  '(-_-)', 'I', 'H'])

# sort(): this numpy ndarray object's method return sorted array(copy)
# without modifying the original one
sorted_arr = np.sort(unsorted_arr)
str_array_sorted = np.sort(str_array)
print("The Sorted Array of The unsorted_arr:", sorted_arr)
print("The Sorted Array of The str_array:", str_array_sorted)
""" Output(Alphabetically / alphanumerically):
The Sorted Array of The str_array: ['(-_-)' 'H' 'I' 'Varsity' 'teacher'] 
"""

# Boolean Array Sorting:
bool_arr = np.array([True, False, False, True, False, True])
sort_bool = np.sort(bool_arr)
print("The Sorted Boolean Array: ", sort_bool)

# 2D array Sorting:
a_2d_ = np.array([[789, 123, 456, 321], [101, 40, 12, 999]])
sort_a_2d_ = np.sort(a_2d_)
print("The Sorted elements within a_2d_: ", sort_a_2d_)
