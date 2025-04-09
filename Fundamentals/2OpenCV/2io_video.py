import os
import cv2

# read video
video_path = os.path.join('.', 'data', 'none.mp4')

video = cv2.VideoCapture(video_path)

# Visualise Video
ret = True
while ret:
    ret, frame = video.read()
    
    if ret:
        cv2.imgshow('frame',frame)
        cv2.waitKey(40)
        
video.release()
cv2.destroyAllWindows() # Such that no spaces allocated
