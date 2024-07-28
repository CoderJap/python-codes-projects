import cv2 as cv

img = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\Face Detection\\image\\2.webp")
# cv.imshow('Face Img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\Face Detection\\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f"Number of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
  cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detetcted Faces',img)


cv.waitKey(0) 
