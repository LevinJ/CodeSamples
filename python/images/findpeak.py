from scipy import signal
import numpy as np
import matplotlib.pyplot as plt



xs = np.arange(0, np.pi, 0.05)
plt.plot(xs)
data = np.sin(xs)
plt.plot(data)
peakind = signal.find_peaks_cwt(data, np.arange(1,10))
print(peakind, xs[peakind], data[peakind])