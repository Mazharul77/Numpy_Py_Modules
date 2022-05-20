# Copy(New Array) & View (original one) of Array in numpy:
import numpy as np
arr_1 = np.array([11, 33, 22, 44])
print("The Original arr_1:", arr_1)

"""Copy: Owns data along with un-affecting the original one if any changes"""
arr_1_cpy = arr_1.copy()
arr_1_cpy[2] = 17
print("After Copying The  arr_1_cpy:", arr_1_cpy)

print("After Copying The  arr_1:", arr_1)
# Base check: Let's check the owning (independence) the data : The copy returns None.
# none(if copy used as doesn't affect each other)
print("\n\t......Base of arr_1_cpy:", arr_1_cpy.base, end="\n\n")


"""View: Doesn't own data &
 if any changes to the original array the view also changes(or affected) and 
 if any changes to the view the original array is affected"""
arr_2 = np.array([88, 22, 49, 55])
print("The Original arr_2:", arr_2)
arr_2_view = arr_2.view()
arr_2_view[0] = "909"
print("(Modified) After Viewing The  arr_2_view:", arr_2_view)
print("(Modified) After Viewing The Original arr_2:", arr_2)

# Base check: Let's check the owning (independence) the data :
# The view returns the original array.
print("\n\t......Base of arr_2_view: ", arr_2_view.base, end="\n\n")


