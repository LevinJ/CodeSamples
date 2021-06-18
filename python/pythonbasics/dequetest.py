from collections import deque
import numpy as np


d = deque(maxlen=3)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d[0])
print(d[-1])

d_array = np.array(d)
print(d_array)