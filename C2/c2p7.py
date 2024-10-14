print("23mca022")
print("Aslam Ismail")
print("12-08-24")
import numpy as np
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
mat_sum=mat1+mat2
mat_diff=mat1-mat2
mat_prod=mat1*mat2
mat_div=mat1/mat2
mat_mult=np.dot(mat1,mat2)
mat_transp=np.transpose(mat1)
diag_sum=np.trace(mat1)
print("Matrix1:\n",mat1)
print("Matrix2:\n",mat2)
print("Matrix sum:\n",mat_sum)
print("Matrix Difference\n",mat_diff)
print("Matrix Element-wise Product:\n",mat_prod)
print("Matrix Element-wise Division:\n",mat_div)
print("Matrix Multiplication:\n",mat_mult)
print("Transpose of matrix 1:\n",mat_transp)
print("Sum of diagonal elements of Matrix1:\n",diag_sum)


