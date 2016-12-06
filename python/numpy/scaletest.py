import numpy as np

a = np.arange(1000)
zero_mean = a - a.mean()
scaled_arr = zero_mean/(zero_mean.max() - zero_mean.min())
print (scaled_arr)