import cv2 as cv
import numpy as np

img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")

cv.imshow('Orig Img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

mask_circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Circle mask',mask_circle)

mask_rectangle = cv.rectangle(blank.copy(),(30,30),(470,470),255,-1)
cv.imshow('Rectangle mask',mask_rectangle)

masked = cv.bitwise_and(img,img,mask=mask_rectangle)
cv.imshow('Masked Img',masked)


cv.waitKey(0)