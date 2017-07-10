import numpy as np

heat_map_img = np.zeros((720,1280,3), dtype=np.uint8)
heat_map_img[0,0,0] = 300
print(heat_map_img[0,0,0])