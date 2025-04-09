# This Code will Open Webcame when run it
import cv2

# Read Webcam (try 0 if 2 doesn't work)
webcam = cv2.VideoCapture(0) # initalise the video cam for video capture

# Visualise Webcam
while True:
    ret, frame = webcam.read() # capture a single frame
    
    cv2.imshow('Darshanframe', frame)  # creates a window and display current frame
    if cv2.waitKey(40) & 0xFF == ord('q'): # waits for 40 millisecondsfora key press
        break
    
webcam.release()
cv2.destroyAllWindows() #Closes all OpenCV windows created during execution
