# ColourSpace
import os
import cv2

img = cv2.imread(os.path.join('.','./Fundamentals/2OpenCV/bird.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Converted to rgb colour space

cv2.imshow('img_of_bird', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)

cv2.waitKey(0)
