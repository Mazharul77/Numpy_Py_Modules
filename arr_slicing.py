
"""
Array Slicing with numpy.....
 slice like this: [start:end] or step, like: [start:end:step] with required position
  but above technique includes the start index & excludes the end index
 """
import numpy as np
# let's apply several slicing......

print("Access & Demonstrate specific index(any range or step) as Slicing:")
arr_list = np.array(["Software", 22, "Engineer", 11, 4, 6, "Mazharul", "Google"])
print("sliced arr_list as a reversed way:", arr_list[::-1])
print("Value/Attributes slicing from 2nd index to before 7th index:", arr_list[2:7])
print("Value/Attributes slicing from 2nd index to last index:", arr_list[2:])
print("Value/Attributes slicing from 2nd index to last index:", type(arr_list[2:]))

# let's implement step slicing.......
print("Return every other element from index 0 to index 7:", arr_list[0:7:2])
print("Return every other element from the entire array:", arr_list[::2])

print("\n\t Return odd position value from entire array:", arr_list[1::2])
print("\t Return even position value from entire array:", arr_list[::2])

# Slicing with n-D array (n-D Matrix):
my_arr2 = np.array([["software", 1, "engineer", 2, 5, 15], [11, 33, 55, 77, 100, 57]])
print("From 2D array we slice 2nd element's(also an array) from index 2 to 4:", my_arr2[1, 2:4])

print("\n\t Slicing index 0 to 4(exclusive) from both elements of my_arr2:", my_arr2[0:2, 0:4])
