#cropping in images
import os
import cv2

img = cv2.imread(os.path.join('.','./Fundamentals/2OpenCV/dogs.jpg'))

print(img.shape)

cropped_img = img[220:740, 320:1040]
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)


