import cv2
import numpy as np


image_name = './temp/sift_basic_0.jpg'
image_name = './temp/img_5.jpg'
image_name = './temp/zero_sift.jpg'
img = cv2.imread(image_name)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT(nfeatures=10,contrastThreshold=4e-12, edgeThreshold=5e10)
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('./temp/sift_keypoints.jpg',img)
kp,des = sift.compute(gray, kp)
print len(kp)
print des.shape