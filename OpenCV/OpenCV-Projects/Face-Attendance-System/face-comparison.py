import cv2 as cv
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\OpenCV-Projects\\Face-Attendance-System\\Images-Train-Test\\elon-2.webp")

imgElon = cv.cvtColor(imgElon,cv.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\OpenCV-Projects\\Face-Attendance-System\\Images-Train-Test\\elon-3.webp")

imgTest = cv.cvtColor(imgTest,cv.COLOR_BGR2RGB)

# Detect faces
faceLocs = face_recognition.face_locations(imgElon)
encodeElon = face_recognition.face_encodings(imgElon)[0]

# Draw rectangles around detected faces
for faceLoc in faceLocs:
    top, right, bottom, left = faceLoc
    cv.rectangle(imgElon, (left, top), (right, bottom), (255, 0, 255), 2)

faceLocsTest = face_recognition.face_locations(imgTest)
encodeTest = face_recognition.face_encodings(imgTest)[0]

# Draw rectangles around detected faces
for faceLoc in faceLocs:
    top, right, bottom, left = faceLoc
    cv.rectangle(imgTest, (left, top), (right, bottom), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon],encodeTest)
faceDist = face_recognition.face_distance([encodeElon],encodeTest)
print(results)
print(faceDist)

cv.putText(imgTest,f"{results} {round(faceDist[0],2)}",(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv.imshow('Elon Test',imgTest)
cv.imshow('Elon Musk',imgElon)

cv.waitKey(0)


