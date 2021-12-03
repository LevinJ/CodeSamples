import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

print(ax)

lines = ax.plot(np.arange(5))

print lines

print ax.lines

lines2 = ax.plot(np.arange(10, 16, 1))

print lines2

print ax.lines
