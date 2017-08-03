import numpy as np
x = np.arange(10).reshape(2,5)
# x[np.nonzero(x>=2)] = 100
y = np.array([0,1])
x[:, (2,2)] = x[:, (2,2)]- 1000
print x