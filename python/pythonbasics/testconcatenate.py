import numpy as np
x = np.arange(4)
y = np.arange(4,8)
z = [x,y]
print(z)
print(np.vstack(z, ))