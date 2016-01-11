import numpy as np
# a = np.arange(12) **2
# i = np.array([1,1,3,8,5])
# print(a[i])

nums = [0,1,2,3,4]
squares = [x **2 for x in nums]
print(squares)
squares2 = [x **2 for x in nums if x%2 ==0]
print(squares2)