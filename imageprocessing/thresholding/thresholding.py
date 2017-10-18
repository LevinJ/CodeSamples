import cv2
import numpy as np
from matplotlib import pyplot as plt

class Thresholding:
    def __init__(self):
        
        return
    def simple(self,img):
        thresh = 50
        ret,thresh1 = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
        ret,thresh2 = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY_INV)
        ret,thresh3 = cv2.threshold(img,thresh,255,cv2.THRESH_TRUNC)
        ret,thresh4 = cv2.threshold(img,thresh,255,cv2.THRESH_TOZERO)
        ret,thresh5 = cv2.threshold(img,thresh,255,cv2.THRESH_TOZERO_INV)
#         titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#         images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
        
        titles = ['Original Image','BINARY']
        images = [img, cv2.bitwise_not(thresh1)]
        for i in range(2):
            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()
        return
    def adaptive(self, img):
        img = cv2.medianBlur(img,5)
        C = -10
        blocksize = 11
        ret,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    cv2.THRESH_BINARY,blocksize,C)
       
        th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,blocksize,C)
        titles = ['Original Image', 'Global Thresholding (v = 127)',
                    'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img, cv2.bitwise_not(th1), cv2.bitwise_not(th2), cv2.bitwise_not(th3)]
        for i in range(4):
            plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()
        return
    def otsu(self, img):
        # global thresholding
        ret1,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
        # Otsu's thresholding
        ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img,(5,5),0)
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # plot all the images and their histograms
        images = [img, 0, cv2.bitwise_not(th1),
                  img, 0, cv2.bitwise_not(th2),
                  blur, 0, cv2.bitwise_not(th3)]
        titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
                  'Original Noisy Image','Histogram',"Otsu's Thresholding",
                  'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
        for i in range(3):
            plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
            plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
            plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
            plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
            plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
            plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
        plt.show()
        return
   
    def run(self):
        img = cv2.imread('1.jpg',0)
#         img = cv2.imread('2.jpg',0)
#         self.simple(img)
#         self.adaptive(img)
        self.otsu(img)
        
        return
    
  
    

    
if __name__ == "__main__":   
    obj= Thresholding()
    obj.run()