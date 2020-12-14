import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('boston',img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray boston', gray)

#blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur boston', blur)

#edge cascade
canny= cv.Canny(blur, 125, 125)
cv.imshow('edge boston', canny)

#dalating de image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated boston', dilated)

cv.waitKey(0)