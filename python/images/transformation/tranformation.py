import cv2
import numpy as np
from matplotlib import pyplot as plt
print(cv2.__version__)

class Transformation:
    def __init__(self):
        return
    def scaling(self):
       
        self.img_trans = cv2.resize(self.img,None,fx=2, fy=2)
#         self.img_trans = cv2.resize(self.img,(500,500))
        
        
        return
    def translation(self):
        rows,cols, _= self.img.shape
        M = np.float32([[1,0,50],[0,1,50]])
        self.img_trans = cv2.warpAffine(self.img, M,(cols,rows))
        return
    def rotation(self):
        rows,cols, _ = self.img.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),45, 2)
        self.img_trans = cv2.warpAffine(self.img,M,(cols,rows))
        return
    def affine_trans(self):
        rows,cols= self.img.shape

        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[200,50],[100,250]])
        M = cv2.getAffineTransform(pts1,pts2)
        self.img_trans = cv2.warpAffine(self.img,M,(cols,rows))


        return
    def perspective_trans(self):
        rows,cols = self.img.shape

        pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
        pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
        
        M = cv2.getPerspectiveTransform(pts1,pts2)
        
        self.img_trans = cv2.warpPerspective(self.img,M,(300,300))
        return
    
    def run(self):
        img = cv2.imread('../temp/sift_basic_0.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('image',img)
        self.img = img
        
#         self.scaling()
#         self.translation()
        self.rotation()
#         self.affine_trans()
#         self.perspective_trans()
        
        
        
        cv2.imshow('image_scaled',self.img_trans)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
   
        return
    
if __name__ == "__main__":   
    obj= Transformation()
    obj.run()