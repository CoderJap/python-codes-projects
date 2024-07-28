import cv2 as cv

# Reading Images
# img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")

# cv.imshow('Coding',img)

# cv.waitKey(0)

# Reading videos 
capture = cv.VideoCapture(0) # 0 is for webcam and u can put the specific path of the video also here to read that video

while True:
  isTrue , frame = capture.read()
  cv.imshow('Video',frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

