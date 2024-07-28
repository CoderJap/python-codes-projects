import cv2 as cv

# img = img  = cv.imread("C:\\Users\\Japjot Singh\\Desktop\\Kotlin\\python-backup-codes\\OpenCV\\images\\2.jpeg")

# cv.imshow('Coding',img)

def rescaleFrame(frame , scale=0.75):
  # works for Images , videos and Live videos
  width = int(frame.shape[1]*scale)
  height = int(frame.shape[0]*scale)

  dimensions = (width,height)

  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
  # works for only Live video
  capture.set(3,width)
  capture.set(4,height)

capture = cv.VideoCapture(0)

while True:
  isTrue , frame = capture.read()

  frame_resized = rescaleFrame(frame,scale=.2)

  cv.imshow('Video',frame)
  cv.imshow('Video Resized',frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()



