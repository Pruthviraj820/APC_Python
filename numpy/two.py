import numpy as np

arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
arr2=arr[:2, ::2]
print(arr2)


arr1=np.array([1,2,3,4,5,6])
print(arr1[::-1])
print(arr1[::-2])