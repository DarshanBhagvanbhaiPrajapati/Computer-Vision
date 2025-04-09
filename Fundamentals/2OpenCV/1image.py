# import cv2

# image = cv2.imread('some_img.png') # will read images
# print(image.shape()) # give height, width and, number of channels

# #image is made by pixels [0,255] in most cases

import os
import cv2

# --- (READ IMAGE) ----

image_path = os.path.join('.','data','none.jpg') #write correct path
img = cv2.imread(image_path)

# --- (WRITE IMAGE) ----
cv2.imgwrite(os.path.join('.','data','none_out.jpg'), img) # As writing image

# --- (VISUALIZE IMAGE)----
cv2.imshow('image', img)
# cv2.waitKey(0) # 0 for number of Seconds for which image has to open

# Similarly for VIDEO we will do to visualise and read video




