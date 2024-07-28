import cv2 as cv


img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")
cv.imshow('Original Img',img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3))
cv.imshow('Gaussian Blur',gauss)


# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# Bilateral 
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)




cv.waitKey(0)
