import numpy as np

res = np.convolve([1, 2, 3], [0, 1, 0.5])
print(res)