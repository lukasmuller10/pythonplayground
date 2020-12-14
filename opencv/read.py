import cv2 as cv

#READING IMAGES
# img = cv.imread('./Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

#READING VIDEOS
capture = cv.VideoCapture(0) #input 0 for webcam

while True:
    isTrue, frame = capture.read()
    canny= cv.Canny(frame, 125, 125)
    dilated = cv.dilate(canny,(7,7),iterations=3)

    cv.imshow('dilated boston', dilated)

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


