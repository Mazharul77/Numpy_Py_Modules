# Exploring/finding indexes corresponding to expected-matched value:
# where() : return indexes of passed value:
import numpy as np
num_arr = np.array([8, 5, 77, 88, 33, 5, 98, 86])
st_arr_1 = np.array(['55', 'bhuiyan', '4', 'software', '557', '123', '55', 'Mazharul', '55', 'bhuiyan'])
st_arr_2 = np.array([55, 4,  557, 23, 55, 55])
print("The num_arr:", num_arr)
print("The String Array::", st_arr_2)

# Let's query/search any element's position as indexes:
indexes_2 = np.where(st_arr_2 == 55)
print("The indexes of 55 is: ", indexes_2)

indexes_1 = np.where(st_arr_1 == 'bhuiyan')
print("The indexes of 'bhuiyan' is: ", indexes_1)
# output description: (array([1, 9], dtype = int64),)
# since 'bhuiyan' is found at index: 1th, 9th

# indexes of even value along with odd values in the array num_arr:
idx_even = np.where(num_arr % 2 == 0)
print("In Index: ", idx_even, "Even Value is (respectively): ", num_arr[idx_even])

# indexes of odd value along with odd values in the array num_arr:
idx_odd = np.where(num_arr % 2 == 1)
print("In Index: ", idx_odd, "Odd Value is (respectively) : ", num_arr[idx_odd])

# searchsorted(): binary search to return indexes of particular value in sorted array
# By-Default search index from left
# but we can search that particular right most one by using params: side = 'right'
st_arr = np.array([2, 4, 5, 23, 23, 23, 46, 51, 56, 66, 77, 80, 84, 99, 100])
srch_idx = np.searchsorted(st_arr, 23)
srch_idx_right = np.searchsorted(st_arr, 23, side='right')

print("The indexes of 23 with searchsorted():", srch_idx)
print("The indexes(right most value) of 23 with searchsorted():", srch_idx_right)

# Multiple specific values searches : return indexes as an array for required sorted position
# if we we want insert multiple values as array in st_arr
# then the indexes as output will place as an array

multi_elem_search = np.array([1, 3, 9, 30, 101])
required_ins_idx = np.searchsorted(st_arr, multi_elem_search)  # [0, 1, 3, 6, 15]
print(multi_elem_search, "would be inserted in:", required_ins_idx, "indexes of st_arr respectively.")