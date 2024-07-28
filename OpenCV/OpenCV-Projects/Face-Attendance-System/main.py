import cv2 as cv
import numpy as np
import face_recognition
import os
from datetime import datetime

path = "C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\OpenCV-Projects\\Face-Attendance-System\\Attendance-Img\\"
Images=[]
classNames = []

myList = os.listdir(path)
print(myList)

for cl in myList:
  currImg = cv.imread(f'{path}{cl}')
  Images.append(currImg)
  classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
  encodeList = []
  for img in images:
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
  return encodeList

def markAttendance(name):
  with open('C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\OpenCV-Projects\\Face-Attendance-System\\Attendance.csv','r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
      entry = line.split(',')
      nameList.append(entry[0])

    if name not in nameList:
      now = datetime.now()
      dString = now.strftime('%H:%M:%S')
      f.writelines(f"\n{name},{dString}")


encodeListKnown = findEncodings(Images)
print('Encoding Completed...')

cap = cv.VideoCapture(0)

while True:
  success , img = cap.read()
  imgS = cv.resize(img,(0,0),None,0.25,0.25)
  imgS = cv.cvtColor(imgS,cv.COLOR_BGR2RGB)

  facesCurrFrame = face_recognition.face_locations(imgS)
  encodeCurrFrame = face_recognition.face_encodings(imgS,facesCurrFrame)

  for encodeFace,faceLoc in zip(encodeCurrFrame,facesCurrFrame):
    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
    faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
    matchIndex = np.argmin(faceDist)

    if matches[matchIndex]:
      name = classNames[matchIndex].upper()

      y1,x2,y2,x1 = faceLoc
      y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
      cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
      cv.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv.FILLED)
      cv.putText(img,name,(x1+6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
      markAttendance(name)

  cv.imshow('WebCam',img)
  cv.waitKey(1)


