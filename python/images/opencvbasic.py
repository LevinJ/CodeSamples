import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread(r'C:\Users\jianz\workspace\neweuronotes\Data\Euro\All genuine Notes\100_IS02\FU\20090119_142911_00.bmp',
                 cv2.IMREAD_GRAYSCALE)


imgdata = img.reshape(-1)
plt.hist(imgdata, 10, normed = True)
plt.show()
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()