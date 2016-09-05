#https://gist.github.com/mweibel/bd2d6c2271e42ed97b97

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\jianz\workspace\neweuronotes\Data\Euro\All genuine Notes\100_IS02\FU\20090119_142911_00.bmp', cv2.IMREAD_GRAYSCALE)


def compute_skew(image):
#     image = cv2.bitwise_not(image)
    height, width = image.shape

    edges = cv2.Canny(image, 230, 245)
    cv2.imshow('edges',edges)
    lines = cv2.HoughLinesP(edges, 1, cv2.cv.CV_PI/180, 2, minLineLength=width / 2.0, maxLineGap=20)
    angle = 0.0
    nlines = lines.size
    for x1, y1, x2, y2 in lines[0]:
        angle += np.arctan2(x2 - x1, y2 - y1)
    return angle / nlines


def deskew(image, angle):
    image = cv2.bitwise_not(image)
    non_zero_pixels = cv2.findNonZero(image)
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)

    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    cols, rows = image.shape
    rotated = cv2.warpAffine(image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)

    return cv2.getRectSubPix(rotated, (cols, rows), center)


deskewed_image = deskew(img.copy(), compute_skew(img))
cv2.imshow('image',img)
cv2.imshow('image_deskewed',deskewed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()