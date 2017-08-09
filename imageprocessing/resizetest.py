import sys
import os

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img_file = '/home/levin/Downloads/udacity_review/diagnostic_view.png'

img = cv2.imread(img_file)

# img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
img = cv2.resize(img, (300, 300))
plt.imshow(img[...,::-1])
plt.imsave('/home/levin/adv.png', img[...,::-1])
plt.show()