# Joining into single array by axes:
# concatenate() : join sequence of array:
import numpy as np

# 1D arrays joining
A1 = np.array(['B', 'a', 'n', 'g', 'l', 'a'])
B1 = np.array(['D', 'e', 's', 'h', 'i', " "])
C1 = np.array(['S', 't', 'u', 'd', 'e', 't'])

AB_1 = np.concatenate((A1, B1, C1))
print("Concatenated 1D Arrays:\n", AB_1)

# 2D array Joining with rows : axis-1
A2 = np.array([[0, 1, 10, 11], [100, 101, 110, 111]])
B2 = np.array([[1000, 1001, 1010, 1011], [1100, 1101, 1110, 1111]])
C2_joined = np.concatenate((A2, B2), axis=1)
print("Concatenated 2D Arrays with axis-1:\n", C2_joined)

# stack(): Stack Function: Joining Array with new axis to put array one over another:
C1_stacked = np.stack((A1, B1, C1), axis=1)
print("Stacking Arrays one over another with new axis:\n")
print(C1_stacked)

# 2D array Stacking:
C2_stacked = np.stack((A2, B2))
print("\n\t Stacking Arrays one over another with new axis(2D):\n")
print(C2_stacked)

# hstack(): stacking along rows(let's do for 1D): [same as concatenate()]
c1_hstack = np.hstack((A1, B1, C1))
print("\n\t hstack: Stacking Along Rows(for 1D):")
print(c1_hstack)

# hstack(): stacking along rows(let's do for 2D):
c2_hstack = np.hstack((A2, B2))
print("\n\t hstack: Stacking Along Rows(for 2D):")
print(c2_hstack)

# vstack() : stacking along columns(1D)
C1_vstack = np.vstack((A1, B1))
print("\n\t vstack: Stacking Along column(for 1D):", C1_vstack)

# vstack() : stacking along columns(2D)
C2_vstack = np.vstack((A2, B2))
print("\n\t vstack: Stacking Along column(for 2D):", C2_vstack)

# dstack(): stacking along height like depth(let's do for 1D):
c1_dstack = np.dstack((A1, B1, C1))
print("\n\t dstack: Stacking Along height like depth(for 1D):")
print(c1_dstack)

# dstack(): stacking along height like depth(let's do for 2D):
c2_dstack = np.dstack((A2, B2))
print("\n\t dstack: Stacking Along height like depth(for 2D):")
print(c2_dstack)

