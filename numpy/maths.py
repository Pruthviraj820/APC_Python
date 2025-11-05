import numpy as np
import math

arr1=np.array([1,2,3,4,5,6])
if arr1.size==math.prod(arr1.shape):
     print("True")

print(np.zeros(2))
print(np.ones(3))
print(np.empty(4))
print(np.arange(2,9,2))