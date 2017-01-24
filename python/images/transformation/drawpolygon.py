import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a black image
# img = np.zeros((512,512,3), np.uint8)

fname = './data/straight15.jpg'
img = cv2.imread(fname)


# Draw a polygon
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))

src = np.float32([(610,451), (683,451), (1142,720),(270,720)])
        
pts = src.reshape((-1,1,2)).astype(np.int32)


cv2.polylines(img,[pts],True,(0,0,255),5)

#Display the image
img = img[...,::-1] #convert from opencv bgr to standard rgb
plt.imshow(img)
plt.show()