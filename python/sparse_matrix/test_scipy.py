from scipy.sparse import random
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(1,15,15)
Y = np.linspace(20,30,10)
xx, yy = np.meshgrid(X,Y)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xx, yy, ls="None", marker=".")
plt.show()