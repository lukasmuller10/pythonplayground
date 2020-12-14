import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Boston', img)

#GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RBG', rgb)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)