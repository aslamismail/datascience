print("23mca022")
print("Aslam Ismail")
print("12-08-24")
import numpy as np;
arr_1d = np.array([1, 2, 3, 4, 5])
diag_mat = np.diag(arr_1d)
print("1D Array:")
print(arr_1d)
print("\nDiagonal Matrix:")
print(diag_mat)
arr_2d_square = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
diag_elements = np.diag(arr_2d_square)
print("\n2D Square Matrix:")
print(arr_2d_square)
print("\nDiagonal Elements:")
print(diag_elements)
arr_2d_non_square = np.array([[1, 2, 3],
[4, 5, 6]])

diagonal_elements_non_square = np.diag(arr_2d_non_square)
print("\n2D Non-Square Matrix:")
print(arr_2d_non_square)
print("\nDiagonal Elements (Non-Square):")
print(diagonal_elements_non_square)