import sys
import os

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math




class Morphological(object):
    def __init__(self):
      
        return
    
    def stack_image_horizontal(self, imgs, max_img_width = None, max_img_height=None):
        return self.__stack_image(imgs, axis = 1, max_img_width = max_img_width, max_img_height=max_img_height)
    def stack_image_vertical(self, imgs, max_img_width = None, max_img_height=None):
        return self.__stack_image(imgs, axis = 0, max_img_width = max_img_width, max_img_height=max_img_height)
    def __stack_image(self, imgs, axis = None, max_img_width = None, max_img_height=None):
        #first let's make sure all the imge has same size
        img_sizes = np.empty([len(imgs), 2], dtype=int)
        for i in range(len(imgs)):
            img = imgs[i]
            img_sizes[i] = np.asarray(img.shape[:2])
        if max_img_width is None:
            max_img_width = img_sizes[:,1].max()
        if max_img_height is None:
            max_img_height = img_sizes[:,0].max()
        for i in range(len(imgs)):
            img = imgs[i]
            img_width = img.shape[1]
            img_height = img.shape[0]
            if (img_width == max_img_width) and (img_height == max_img_height):
                continue
            imgs[i] = cv2.resize(img, (max_img_width,max_img_height))
            
            
        #stack the image
        for i in range(len(imgs)):
            img = imgs[i]
            if len(img.shape) == 2:
                #if this is a binary image or gray image
                if np.max(img) == 1:
                    scaled_img = np.uint8(255*img/np.max(img))
                else:
                    scaled_img = img
                imgs[i] = cv2.cvtColor(scaled_img, cv2.COLOR_GRAY2BGR)
#                 plt.imshow(imgs[i][...,::-1])
        res_img = np.concatenate(imgs, axis=axis)
        return res_img
    def find_texts(self, fname):
        img = cv2.imread('j.png',0)
        
        #erosion
        kernel = np.ones((5,5),np.uint8)
        self.erosion = cv2.erode(img,kernel,iterations = 1)
        
        #dilation
        self.dilation = cv2.dilate(self.erosion,kernel,iterations = 1)
        
        
        #opening
        
        self.opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        
        self.closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        
        self.gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
      
        self.img = img
        return
    
        
    def run(self):
        
        fnames = ['./j.png']

        res_imgs = []
        for fname in fnames:
            print("image {}".format(fname))
            self.find_texts(fname)
            res_imgs.append(self.stack_image_horizontal([self.img, self.erosion, self.dilation,self.opening, self.closing, self.gradient]))
           
        
        res_imgs = self.stack_image_vertical(res_imgs)
        
        res_imgs = res_imgs[...,::-1]
        plt.imshow(res_imgs)
        
        plt.show()
        return



if __name__ == "__main__":   
    obj= Morphological()
    obj.run()