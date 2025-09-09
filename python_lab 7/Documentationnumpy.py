import numpy as np

# Arrray creation
#np.array(): Create an array from a list or tuple
arr = np.array([3,4,5])
print("Array:",arr)

#np.zeros():Create an array filled with zeros.
zeros = np.zeros((2,3))
print("Zeros Array:",zeros)

#np.ones():Create an array filled with ones.
ones = np.ones((2,3))
print("Ones Array:",ones)

#np.arange():Create an array with a range of values.
range1 = np.arange(1,10,1)
print("Range Array:", range1)

#np.linspace(): Create an array with evenly spaced values.
linspace1 = np.linspace(2,1,10)
print("Linspace Array:",linspace1)

#2. Array Manipulation
#np.reshape(): Reshape an array.
reshape1= np.reshape(np.arange(6),(2,3))
print("Reshape Array:", reshape1)

#np.transpose ():Transpose an array.
transposed1 = np.transpose(np.array([[1,2], [3,4]]))
print("Transposed Array:",transposed1)

#3. Mathematical operations
# np.add() : Add arrays element-wise.
sum_arr1 = np.add([1,2],[3,4])
print("sum Array:",sum_arr1)

#np.substract() : Substract arrays element-wise.
sub_arr1 = np.subtract([3,4],[1,2])
print("Substract Array:", sub_arr1)

#np.multiply(): Multiply arrays element-wise.
prod_arr1 = np.multiply([1,2],[3,4])
print("Multiply Array:",prod_arr1)

#np.divide(): Divide arrays element-wise.
div_arr1 = np.divide([1,2],[3,4])
print("Divide Array:", div_arr1)

#4. Statical Function
#np.median(): Compute the median.
median1 = np.median([1,2,3])
print("Median:",median1)

#np.mean(): Compute the mean.
mean1 = np.mean([1,2,3])
print("Mean:",mean1)

#np.std(): Compute the standard deviation.
std1 = np.std([1,2,3])
print("Standaed Deviation :",std1)

#np.var(): Compute the variance.
var1 = np.var([1,2,3])
print("Variance:",var1)

#5.Linear Algebra
#np.dot(): Compute the dot product.
dot_prod1 = np.dot([1,2],[3,4])
print("Dot Product:",dot_prod1)

#np.linalg.inv(): Compute the inverse of a matrix.
matrix1 = np.array([1,2],[3,4])
inv_matrix1 = np.linalg.inv(matrix1)
print("Inverse Matrix:",inv_matrix1)

#6. Random numbers
#np.random.rand() : Generate random numbers from a uniform distribution.
rand1 = np.random.rand(2,3)
print("Uniform random Array:",rand1)

#np.random.randn():Generate randoom numbers from a normal distribution.
rand2 = np.random.randn(2,3)
print("Random Normal Array:",rand2)

#7. Logical Oprations
#np.all(): Test if all elements are True.
all_T = np.all([True,True])
print("All true:",all_T)

#np.any() : Test if any elements is True.
any_T = np.any([True,False])
print("Any true:",any_T)