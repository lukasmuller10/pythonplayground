import cv2 as cv

#READING IMAGES
# img = cv.imread('./Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

#READING VIDEOS
capture = cv.VideoCapture(0) #input 0 for webcam

while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray, 3)
    canny= cv.Canny(blur, 125, 125)
    dilated = cv.dilate(canny,(7,7),iterations=3)
    ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

    cv.imshow('dilated boston', dilated)

    cv.imshow('Thresh',thresh)

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


