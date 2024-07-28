import numpy as np 
import cv2 as cv

PATH = 'C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\Face Detection\\'

haar_cascade = cv.CascadeClassifier(f'{PATH}haar_face.xml')

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

# features = np.load(f'{PATH}features.npy',allow_pickle=True)
# labels = np.load(f'{PATH}labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(f'{PATH}face_trained.yml')

img = cv.imread(r'C:\Users\Japjot Singh\Desktop\Kotlin\python-backup-codes\OpenCV\Face Detection\Faces\val\mindy_kaling\2.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

# Detect face
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for(x,y,w,h) in faces_rect:
  faces_roi = gray[y:y+h,x:x+w]

  label,confidence = face_recognizer.predict(faces_roi)
  print(f'Label = {people[label]} with a confidence of {confidence}')

  cv.putText(img , str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
  cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)


cv.waitKey(0)
