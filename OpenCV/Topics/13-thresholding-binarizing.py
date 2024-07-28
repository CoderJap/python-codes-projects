import cv2 as cv
import numpy as np

img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")
cv.imshow('Original img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Single Thresholding
threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY) # set values greater than 150 to 255 and others to 0 
cv.imshow('Simple Thresholded',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # set values lesser than 150 to 255 and others to 0 
cv.imshow('Thresh Inv',thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,5)
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)
