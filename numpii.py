import numpy as np

# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

#check version
print(np.__version__)


print("-------- tuple array ----------")
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method
tarr = np.array((1, 2, 3, 4, 5))
print(tarr)


print("-------- 0D array ----------")
#0-D Arrays
zarr = np.array(42)
print(zarr)


print("-------- 1D array ----------")
# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
#check array type
print(type(arr1))
for a in arr1:
    print(a)
    
    
print("-------- 2D array ----------")
# 2D array
arr2= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print("-------------")
for b in arr2:
    for t in b:
        print(t)
    

print("-------- 3D array ----------")
# 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print("-------------")
for ele in arr:
    for x in ele:
        for z in x:
            print(z)

print("-------- add multi number dimensions array ----------")
darr = np.array([1, 2, 3, 4], ndmin=7)
print(darr)
print('number of dimensions :', darr.ndim)


print("-------- Slicing arrays ----------")
sliarr = np.array([1, 2, 3, 4, 5, 6, 7])
print(sliarr[1:5])

print("-------- Joining NumPy Arrays ----------")

conarr1 = np.array([1, 2, 3])

conarr2 = np.array([4, 5, 6])

concatarr = np.concatenate((conarr1,conarr2))

print(concatarr)

print("-------- Splitting NumPy Arrays ----------")

splits = np.array([1, 2, 3, 4, 5, 6, 7])
RRr = np.array_split(splits, 4)
print(RRr)

print("-------- Searching Arrays ----------")

sear=np.array([1,3,2,4,6,7,3,3])
indexx = np.where(sear == 3)
print(indexx)

print("-------- Sorting Arrays ----------")

sorting = np.array([5,9,3,4,99,1,66])

sor = np.sort(sorting)
print(sor)

