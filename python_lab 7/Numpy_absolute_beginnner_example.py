# This file contains examples from official Numpy guide for absolute beginners:
#https://numpy.org/devdocs/user/absolute_beginners.html

import numpy as np


#1. Creating an array.
#Creating a 1D array.
arr1 = np.array([1,2,3,4,5])
print("1D Array:",arr1)

#Create 2D array.
arr3 = np.array([[1,2,3],[4,5,6]])
print("2D Array:",arr3)

#Creating an array with specific data type.
arr2 = np.array([1,2,3,4,5],dtype= float)
print('Float Array:',arr2)

#2. Inspecting Arrays.
#Check the shape of an array.
print("Shape of arr1:",arr3.shape)

#Check the data type of an array.
print("Data type of float array:",arr2.dtype)

#check the size of an array.
print("sice of arr1 :",arr1.size)

#3.Array Operations.
#Element -wise addition.
add1 = arr1 + 5
print("Element-wise addition:",add1)

#Element-wise multiplication.
multi1 = arr1 *2
print("Element-wise multiplication:",multi1)

#Element-wise power.
power1 = arr1 ** 2
print("Element-wise power:",power1)

#4.Array Indexing and Slicing.
#Indexing
index1 = arr1[2]
print("Indexing:",index1)

#Slicing.
Slice1 = arr1[1:4]
print("Slicing (2nd to 4th element):",Slice1)

#5. Reshaping an array.
reshaped1 = arr1.reshape((1,5))
print('Reshaped Array:',reshaped1)

#6.Combining Arrays.
#Concatenate two arrays.
conatenated1 = np.concatenate((arr1,arr2))
print("Concatenated Array:",conatenated1)

#Stack two arrays vertically.
vstacked1 = np.vstack((arr1,[6,7,8,9,10] ))
print("Vertically stacked Array:",vstacked1)

#Stack two arrays horizontally.
hstacked1 = np.hstack((arr1,[6,7,8,9,10]))
print("Horizontally stacked Array:",hstacked1)

#7. Splitting an array.
#splitting an  array into multiple cub arrays.
split1 = np.array_split(arr1,3)
print("Split Array:",split1)

#8. copying Arrays.
#Create a copy of an array.
copy = arr1.copy()
copy[0]= 99
print("Original Array:",arr1)
print("Copied Array:",copy)

#Mathematical functions.
#Compute the mean.
mean1 = np.mean(arr1)
print("Mean:",mean1)

#Compute the standard deviation
std1 = np.std(arr1)
print("Standard Deviation:",std1)

#compute the sum.
sum1 = np.sum(arr1)
print("Sum:",sum1)

#compute the product.
prod1 = np.prod(arr1)
print("Product:",prod1)

