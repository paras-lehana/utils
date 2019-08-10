#Colab: https://colab.research.google.com/drive/1z-p9F8YmAnLrAGaNQ-lkZpHTqbwGLvSy

import numpy as np
from numpy import linalg as la

import math

def eigen(matrix):
  
  eigenValues, eigenVectors = la.eig(matrix)

  idx = eigenValues.argsort()[::-1]
  eigenValues = eigenValues[idx]
  eigenVectors = eigenVectors[:,idx]
  
  return eigenValues, eigenVectors
  
#matrixA = np.array([[1,0,1,0],[0,1,0,1]])
matrixA = np.array([[2,4],[1,3],[0,0],[0,0]])
#matrixA = np.array([[5,5],[-1,7]])
#matrixA = np.array([[3,1,1],[-1,3,1]])

#matrixA = np.array([[4,0],[3,-5]])
n,p = np.shape(matrixA)

print("\n\n-----------------\n\nMatrix A:\n")
print(matrixA)

matrixAAT = np.dot(matrixA,matrixA.transpose())
matrixATA = np.dot(matrixA.transpose(),matrixA)

print("\n\n-----------------\n\nMatrix AAT:\n")
print(matrixAAT)
print("\n\n-----------------\n\nMatrix ATA:\n")
print(matrixATA)

eigenValues, eigenVectors = eigen(matrixAAT)

matrixU = eigenVectors
print("\nEigen Values:\n")
print(eigenValues)

print("\n\n-----------------\n\nMatrix U:\n")
print(matrixU)

matrixS = np.vectorize(math.sqrt, otypes=[float])(eigenValues.reshape(n,1)*np.eye(n,M=p, dtype=int))
print("\n\n-----------------\n\nMatrix S:\n")
print(matrixS)

eigenValues, eigenVectors = eigen(matrixATA)

matrixV = eigenVectors
print("\nEigen Values:\n")
print(eigenValues)

print("\n\n-----------------\n\nMatrix V:\n")
print(matrixV)

matrixSVD = matrixU.dot(matrixS).dot(matrixV.transpose())
print("\n\n-----------------\n\nMatrix SVD = A ?:\n")
print(matrixSVD)

print("\n\n-----------------\n\nMatrix SVD by formula:\n")
u,s,vt = la.svd(matrixA)

print("-----------------\n\nMatrix U:\n")
print(u);

print("-----------------\n\nMatrix S:\n")
print(s);

print("\n\n-----------------\n\nMatrix V:\n")
print(v);
