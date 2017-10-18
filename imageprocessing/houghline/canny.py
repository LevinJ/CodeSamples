import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('../thresholding/1.bin.png',0)
edges = cv2.Canny(img,100,150)
plt.subplot(131),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

img = cv2.bitwise_not(img)
plt.subplot(133),plt.plot(img.sum(axis=0))
plt.title('histogram'), plt.xticks([]), plt.yticks([])
plt.show()