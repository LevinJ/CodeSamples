


import numpy as np



pad = 1
erosion = np.ones([5,5])
erosion[:,0:pad] = 0
erosion[:,-pad:] = 0
erosion[0:pad, :] = 0
erosion[-pad:, :] = 0

print(erosion)