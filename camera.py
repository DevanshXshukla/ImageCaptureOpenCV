import cv2
import time
cam=cv2.VideoCapture(0)
time.sleep(1)
img=cam.read()[1]
cv2.imwrite("imgclicked.jpg",img)
cam.release()

