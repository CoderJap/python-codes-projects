import cv2 as cv
import numpy as np

img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")

cv.imshow('Coding',img)

blank = np.zeros(img.shape[:2],dtype='uint8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

# ret , thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Threshold',thresh)

contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!")

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)


cv.waitKey(0)
