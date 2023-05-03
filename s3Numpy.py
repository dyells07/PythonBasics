import numpy as np
import random

#create a numpy array
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1)

#creating 2 dimensional array
array2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2)

#create a 4 dimensional array
array3 = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(array3)


#check the dimension of the array
print(array1.ndim)
print(array2.ndim)  

#check the shape of the array
print(array1.shape)
print(array2.shape)

#printing the data type of the array
print(array1.dtype)
print(array2.dtype)

#creating an array with a defined data type
array4 = np.array([1,2,3,4,5], dtype='S')#S is for string

#converting the data type of an array
array5 = array4.astype('f') #f is for float

#creating an array of shape (10,2) with only zeros
array0 = np.zeros((10,2))
print(array0)

print(array0.dtype)

#creating an array of shape (10,2) with only ones
arrayone = np.ones((10,2))
print(arrayone)


#creating an array of shape (7,2,3 ) with random values
arrayrandom = np.random.random((7,2,3))

print(arrayrandom)