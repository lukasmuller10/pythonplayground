import cv2 as cv 

#RESIZE AND RESCALE IMAGES AND VIDEOS

def rescaleFrame(frame, scale=0.75):
    #images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #live videos
    capture.set(3,heigth)
    capture.set(4.width)

img = cv.imread('./Resources/Photos/cat.jpg')
resized_img = rescaleFrame(img)

cv.imshow('Cat', img)
cv.imshow('Resized Cat', resized_img)

capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.2) 

    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

