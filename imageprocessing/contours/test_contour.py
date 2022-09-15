import numpy as np
import cv2
import matplotlib.pyplot as plt
from utility.duration import Duration

class TestContour(object):
    def __init__(self):
        return 
    def test_sim(self):
        img = np.zeros((1080, 1920, 3),dtype=np.uint8)
        contours = np.array( [[ [50,50], [50,1000], [1500, 1000], [1500,50] ] ])
        
        cv2.drawContours(img, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)
        
        contours = np.array( [[ [1600,50], [1800,50], [1800, 100], [1600,100] ] ])
        
        
        cv2.drawContours(img, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)
         
        img2 = img.copy()
        
        thres = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        
        
        contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours(img, contours, 1, (0,255,0), 3)
        plt.imshow(img)
        plt.show()
        return
    def test_seg_img(self):
        img = cv2.imread("/home/levin/workspace/data/semantic_marks/Zf/seg/label/1657504041732855235.png")
        
        
        # 
        
        # img3 = np.zeros(img.shape[:2], dtype=np.uint8)
        # img3[np.all(img == (255,255,255), axis=-1)] = 10
        # img3[np.all(img == (255,255,0), axis=-1)] = 11
        
        tk = Duration()
        # roadmark_flag = np.all(img == (255,255,255), axis=-1) | np.all(img == (255,255,0), axis=-1)
        # thres = np.zeros(img.shape[:2], dtype=np.uint8)
        # thres[roadmark_flag] = 255
        thres = cv2.inRange(img, (0, 255, 0), (255, 255, 255))
        print("thres time={:.03f}".format(tk.end()))
        # plt.figure()
        # plt.imshow(thres, cmap="gray")
        
        # 
        # 
        
        
        tk.start()
        contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        print("find contour time={:.03f}".format(tk.end()))
        # cv2.drawContours(img, contours, 2, (0,255,0), 1)
        
        cnt = contours[2]
        M = cv2.moments(cnt)
        print( M )
        area = cv2.contourArea(cnt)
        # perimeter = cv2.arcLength(cnt,True)
        
        
        for ind  in range(len(contours)):
            cnt = contours[ind]
            u, v = cnt[0][0]
            if np.any(img[v, u] != [255, 255, 0]):
                continue
            tk.start()
            epsilon = 2
            app_contours = cv2.approxPolyDP(cnt,epsilon,True)
            # if len(app_contours) <= 6:
            #     continue
            print("appror {}, before= {}, arfter={}".format(ind, len(cnt), len(app_contours)))
            print(app_contours)
            # print("approxPolyDP time={:.03f}".format(tk.end()))
            cv2.drawContours(img, [app_contours], -1, (0,255,0), 1)
            
            tk.start()
            x,y,w,h = cv2.boundingRect(app_contours)
            print("bounding box time={:.03f}".format(tk.end()))
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            
            #rotated boudnig box
            # cnt2 = cnt.reshape((-1, 2))
            # cnt2 = np.concatenate([cnt2, np.zeros([len(cnt2), 1])], axis = -1).astype(np.int32)
            
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(img,[box],0,(0,0,255),2)
            
            #fit a line
            [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
            lefty = int((-x*vy/vx) + y)
            # righty = int(((cols-x)*vy/vx)+y)
            
        plt.figure()
        plt.imshow(img[...,::-1])
        plt.show()
        return
    def run(self):
        self.test_seg_img()
        # self.test_sim()
        return

if __name__ == "__main__":   
    obj= TestContour()
    obj.run()
