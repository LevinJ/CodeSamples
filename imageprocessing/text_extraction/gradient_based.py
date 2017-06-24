import sys
import os

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math



class Findlines(object):
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
        self.large = cv2.imread(fname)
        
        #downsample and use it for processing
        self.rgb = cv2.pyrDown(self.large);
        self.small = cv2.cvtColor(self.rgb,  cv2.COLOR_BGR2GRAY);
        
        #morphological gradient
        morphKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3));
        self.grad = cv2.morphologyEx(self.small, cv2.MORPH_GRADIENT, morphKernel);
        
        #binarize
    
        thres, self.bw = cv2.threshold(self.grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
        
        #connect horizontally oriented regions
        morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1));
        self.connected = cv2.morphologyEx(self.bw, cv2.MORPH_CLOSE, morphKernel);
        
        
        
        #find contours
        im2, contours, hierarchy = cv2.findContours(self.connected.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        self.res = self.small.copy()
        
        self.res = self.rgb.copy()
        mask = np.zeros(self.rgb.shape[:2], np.uint8)
        
        # filter contours
        for idx in range(0, len(contours)):
            x, y, rect_width, rect_height = cv2.boundingRect(contours[idx])
            if rect_height < 16 or rect_width < 16:
                continue
            cv2.drawContours(mask, contours, idx, 255, cv2.FILLED)
            maskroi = mask[y:y+rect_height, x:x+rect_width]
            r = float(cv2.countNonZero(maskroi)) / (rect_width * rect_height)
            
#             plt.imshow(mask, cmap='gray')
            
            
            
            if r > 0.45:
             
#                 cv2.drawContours(self.res, contours, idx, (0, 255, 0))
                cv2.rectangle(self.res, (x, y+rect_height), (x+rect_width, y), (0,255,0),3)
                
            
            # ratio of non-zero pixels in the filled region
#             r = float(cv2.countNonZero(mask)) / (rect_width * rect_height)
#             if r > 0.45 and rect_height > 8 and rect_width > 8:
#                 
#                 cv2.rectangle(self.res, (x, y+rect_height), (x+rect_width, y), (0,255,0),3)

        return
    
        
    def run(self):
        
        fnames = ['./1.jpg']

        
#         fnames = ['./data/ocr/00000012AI20160328023.jpg','./data/ocr/00000015AI20160328023.jpg',
#                   './data/ocr/00000015AI20160127014.jpg','./data/ocr/00000026AI20160329003.jpg',
#                   './data/ocr/00000031AI20160325010.jpg','./data/ocr/00000030AI20160329003.jpg',
#                   './data/ocr/00000026AI20160325020.jpg']
#         
        res_imgs = []
        for fname in fnames:
            print("image {}".format(fname))
            self.find_texts(fname)
#             res_imgs.append(self.stack_image_horizontal([self.res]))
            res_imgs.append(self.stack_image_horizontal([self.small,self.grad, self.bw, self.connected,self.res]))
           
        
        res_imgs = self.stack_image_vertical(res_imgs)
        
        res_imgs = res_imgs[...,::-1]
        plt.imshow(res_imgs)
        
        plt.show()
        return



if __name__ == "__main__":   
    obj= Findlines()
    obj.run()
    
#         self.sobelx = cv2.Sobel(self.small, cv2.CV_8U, 1, 0)
#         self.sobely = cv2.Sobel(self.small, cv2.CV_8U, 0, 1)
#         
#         self.sobel = np.sqrt(np.square(self.sobelx) + np.square(self.sobely))
#         self.sobel = np.uint8(255*self.sobel/np.max(self.sobel))
#         
#         self.absgraddir = np.absolute(np.arctan(self.sobely/self.sobelx.astype(np.float)))
#         self.absgraddir = np.uint8(255*self.absgraddir/np.max(self.absgraddir))
         
        
        #morphological gradient