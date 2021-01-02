import cv2 as cv
import numpy as np

# img = cv.imread('./Resources/Photos/lady.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors = 3)

# print(len(faces_rect))

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)

# cv.imshow('Person',img)
# cv.waitKey(0)

capture = cv.VideoCapture(0) #input 0 for webcam

while True:
    isTrue, frame = capture.read()

    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors = 3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
