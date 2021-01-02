import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Cats', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian  
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel 
sobelx = cv.Sobel(gray,  cv.CV_64F,1,0)
sobely = cv.Sobel(gray,  cv.CV_64F,0,1)
cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)

sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel', sobel)

canny = cv.Canny(img, 150,175)
cv.imshow('Canny', canny)
cv.waitKey(0)