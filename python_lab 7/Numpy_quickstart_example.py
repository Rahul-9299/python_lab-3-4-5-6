# This file contains examples from official Numpy quickstart guide.
#https://numpy.org/doc/stable/user/quickstart.html


import numpy as np
#1. The Basics
#Create an array
arr = np.array([1,2,3,4])
print("Array:",arr)

#Create a multidimensional array
multi_arr = np.array([[1,2,3],[4,5,6]])
print("Multidimensional Array:", multi_arr)

#Check the shape of an array
print("Shape of array:", arr.shape)

#Create an array with specific data types
array1 = np.array([1,2,3], dtype = float)
print("float Arrya:",array1)

#2. Array Creation 
#Create  an array of zeros.
zeros1 = np.zeros((2,3))
print("Zeros Array:",zeros1)

#Create an array of ones.
ones1 = np.ones((2,3))
print("Ones Array:",ones1)

#Create an empty array.
empty1 =np.empty((2,3))
print("Empty Array:",empty1)

#Create an array with a range of values.
arange1 =np.arange(1,10,2)
print("Arange array:",arange1)

#Create an array with evenly spaced value.
linspace1 = np.linspace(0,1,5)
print("Linespace Array:",linspace1)

#3.Basic operations
#Element-wise additon.
addition1 = np.array([1,2,3]) + np.array([4,5,6])
print("Addition array:",addition1)

#Element-wise multiplication.
multiplication1 = np.array([1,2,3]) * np.array([4,5,6])
print("Multiplication Array:",multiplication1)

#Matrix multiplication.
matrix_mult1 =np.dot(np.array([[1,2],[3,4]]),np.array([[5,6],[7,8]]))
print("Matrix Multiplication:",matrix_mult1)

#4. Universal function.
#Compute the sine of an array.
sine = np.sin(np.pi/2)
print("Sine:",sine)

#Compute the exponential of an array.
exponential = np.exp(np.array([1,2,3]))
print("Exponential:",exponential)

#Compute the squae root of an array.
square_root= np.sqrt([1,4,9])
print("Square root:",square_root)

#5.Indexing, Slicing and Iterating.
#Indexing
indexing1 =np.array([1,2,3,4,5])[2]
print("Indexing:",indexing1)

#Iterating
iterating1 = [x for x in np.array([1,2,3])]
print("Iterating:",iterating1)

#Slicing
slicing1 = np.array([1,2,3,4,5])[1:4]
print("Slicing:",slicing1)

#6.shape Manipulation
#Reshape an array.
reshaped = np.arange(6).reshape((2,3))
print("Reshaped Array:",reshaped)

#Transpose an array.
transposed = reshaped.T
print("Transposed Array:",transposed)

#7.Stacking and Splitting
#Stack arrays verically.
vstacked = np.vstack((np.array([1,2,3]),np.array([4,5,6])))
print("Vertically Stacked Array:",vstacked)

#stacked arrays horizontally.
hstacked = np.hstack((np.array([1,2,3]),np.array([4,5,6])))
print("Horizantally Stacked Array:", hstacked)

#split an array.
split1 = np.hsplit(np.array([[1,2,3],[4,5,6]]),3)
print("Split Array:",split1)

#8.Copying and Views
#Create a view of an array.
original = np.array([1,2,3])
view1 = original.view()
view1[0] = 99
print("Original Array:", original)
print("View Array:",view1)

#Create a copy of an array.
copy1 = original.copy()
copy1[0] =0
print("Original Array after copy:",original)
print("Copy Array:",copy1)

#9.Linear Algebra
#Compute the inverse of a matrix
matrix1 = np.array([[1,2],[3,4]])
inverse1 = np.linalg.inv(matrix1)
print("Inverse of Matrix:",inverse1)

#compute the eigen values of a matrix
eigen_values, eigen_vectors = np.linalg.eig(matrix1)
print("'Eigen Values:",eigen_values)
print("'eigen Vectors:",eigen_vectors)

#Solve a linear system of equations
coefficient =np.array([[3,1],[1,2]])
constants = np.array([9,8])
solution = np.linalg.solve(coefficient,constants)
print("Solution of linear equations :",solution)




