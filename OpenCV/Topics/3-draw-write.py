import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")
# cv.imshow('Coding',img)

# 1. Paint the image a certain color
# blank[:] = 0,0,255
# blank[200:300,300:400] = 0,0,255
# cv.imshow('Colored Img',blank)

# 2.Draw a rectangle 
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
# cv.imshow("Rectangle",blank)

# 3.Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# 4.Draw a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('Text',blank)



















cv.waitKey(0)