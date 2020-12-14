import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny = cv.Canny(gray, 125, 125)
cv.imshow('canny',canny)

cv.waitKey(0)