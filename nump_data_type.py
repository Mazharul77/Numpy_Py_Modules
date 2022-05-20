""" Besides regular data-types in numpy the extra data types are also can be represent with their acronyms
like i(integer), f(float), c(complex data-type), b(boolean), u(unsigned integer),  m(time delta),
M(dateTime), O(Object), S(String), U(unicode String), V(fixed chunk of memory for other data type), etc
"""
# dtype:  numpy array object's property( to return the type of object of the data)

import numpy as np
collection = np.array([1, 44, 67])
print("The datatype of collection:", collection.dtype)

# creating String data type:
coll_new = np.array([11, 1234567, 42, 63], dtype='S')
print("Created array with defined type:", coll_new)
print("The type of coll_new:", coll_new.dtype)

#  array with data type 4 bytes integer
my_arr = np.array([420.0, 2.4, 4.0, 0.5], dtype="i4")
print("\n\t Array Creation with data type 4 bytes integer:", my_arr)
print("\t Array  data type of my_arr:", my_arr.dtype)

# Conversion of data type on existed array: By making a copy with astype() method:
my_arr_S = my_arr.astype('S')
print("\nFloat to String of my_arr:", my_arr_S)
print("Type of my_arr_S:", my_arr_S.dtype)

my_arr_I = my_arr.astype('i')
print("Float to Integer of my_arr:", my_arr_I)
print("Type of my_arr_I:", my_arr_I.dtype)
