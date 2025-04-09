#resizing

import os
import cv2

img = cv2.imread(os.path.join('.','./Fundamentals/2OpenCV/dogs.jpg'))

resized_img = cv2.resize(img, (640, 480))

print(img.shape) #will print dimensions oe original
print(resized_img.shape) #resized dimensions


cv2.imshow('img', img) # Will show original image
cv2.imshow('resized_img', resized_img) # Will show resized image
cv2.waitKey(0) #open till not enter space

#as (640,480) in code but when we change in output 
# it will be (height and weight) i.e (480,640) in ouput



