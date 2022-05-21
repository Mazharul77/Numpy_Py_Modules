"""
Filtering array along with boolean index list
 of corresponding existing/non existing elements/values:
 If False of corresponding index then value is not existing within that array
 if True value/element is existed.
"""
import numpy as np

mzl_ar = np.array([123, 22, 44, 1, 5, 6])
# Array creation from index 0, 1 and 3:
def_arr_list = [True, True, False, True, False, False]
custom_arr = mzl_ar[def_arr_list]  # [123, 22, 1] corresponding of [0, 1, 3]-True-indexes
print("The Declared Array's Value Corresponding to True-Bool Index: ", custom_arr)

"""
Output look like:
 The Declared Array's Value Corresponding to True-Bool Index:  [123  22   1]
 """

# Conditional Filter Array Creation:
# like for values greater than 1 and less than 100: return True otherwise False
# first declaring empty list:
filter_storage_ = []
for value in mzl_ar:
    if (value > 1) and (value < 100):
        filter_storage_.append(True)
    else:
        filter_storage_.append(False)

print("The Generated Boolean Array", filter_storage_)
print(filter_storage_, "-Corresponding True-Array Values of mzl_ar:", mzl_ar[filter_storage_])
print("Original Array-mzl_ar: ", mzl_ar)
print("Indexes of True-Array Values of mzl_ar: ")
for idx_ in np.ndenumerate(mzl_ar[filter_storage_]):
    print(idx_)

# odd element accessing:
odd_ = []
for val in mzl_ar:
    if val % 2 == 1:
        odd_.append(True)
    else:
        odd_.append(False)

print("The Generated For Odd Boolean Array", odd_)
print(odd_, "-Corresponding True-Array Values of mzl_ar:", mzl_ar[odd_])
print("Original Array-mzl_ar: ", mzl_ar)
print("Indexes of True-Array Values of mzl_ar: ")
for odx_ in np.ndenumerate(mzl_ar[odd_]):
    print(odx_)

"""
Directly Filtering array without using iterable variable:
Like even values in mzl_ar:
"""
even_filter_ = mzl_ar % 2 == 0  # return boolean-values of even values
print("Whether Even-Values Truth values of mzl_ar: ", even_filter_)
print("The Even-Values of mzl_ar: ", mzl_ar[even_filter_])
