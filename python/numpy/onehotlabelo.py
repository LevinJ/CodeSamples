import numpy as np
num_labels = 10
labels = np.array([1,1,1,0,2,0])

labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
print labels