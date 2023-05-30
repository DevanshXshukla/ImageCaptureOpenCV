import cv2
import imutils
img=cv2.imread("pythonn.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg",gray)
cv2.imshow("gray.jpg",gray)
thres=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresimg.jpg",thres)
cv2.imshow("thresimg.jpg",thres)
rectimg=cv2.rectangle(img,(10,10),(1500,1500),(0,255,0),10)
textimg=cv2.putText(img,'hello there',(1500,1500),cv2.FONT_HERSHEY_SIMPLEX,30,(0,255,0),2)
cv2.imwrite("imgwithtext.jpg",textimg)
cv2.imwrite("imgwithrect.jpg",rectimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
