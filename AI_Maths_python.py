from math import e
import numpy as np
array1=[[1, 2], [3, 4]]
print(array1)
#detrmnlnt ofa matrix
matrix = np.array(array1)
determinant = np.linalg.det(matrix)
print( determinant)  
#inverse of a matrix
inverse = np.linalg.inv(matrix)
print( inverse) 
#adtion of two matrices 
array2=[[10,34],[17,96]]

result = [[0,0],[0,0]]

for i in range(len(array1)):
    for j in range(len(array1[0])):
        result[i][j] = array1[i][j] + array2[i][j]

for r in result:
    print(r)
#multplaction of two matricis 

for i in range(len(array1)):
    for j in range(len(array2[0])):
        for k in range(len(array2)):
           result[i][j] += array1[i][k] * array2[k][j]


for r in result:
    print(r)

transpose= np.transpose(array1)
print(transpose)


eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)