import tensorflow as tf
import tensorflow.contrib.slim as slim
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2


raw_image = cv2.imread('/home/levin/workspace/snrprj/snr/data/process_result/snrimgs/sample_test/batch_1/DOWN/20171017162233_F004F21727_top_right.jpg', 0).astype(np.float32)/255.


def rotate_img_180(img):
    
    scale = 1
    skew = 180
    height, width = img.shape[:2]
 
    center = (int(width/2), int(height/2))
    rotation_matrix = cv2.getRotationMatrix2D(tuple(center), skew, scale)
    img_rotation = cv2.warpAffine(img, rotation_matrix, (width, height))
    return img_rotation


img_rotation = rotate_img_180(raw_image)
row, col = 1,2
plt.subplot(row, col,1),plt.imshow(np.squeeze(raw_image), 'gray')
plt.subplot(row, col,2),plt.imshow(np.squeeze(img_rotation) , 'gray')
plt.show()
    
    
    
   

    
   
 