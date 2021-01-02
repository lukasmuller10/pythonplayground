import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simples thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)  
cv.imshow('threshold', thresh)

#Inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  
cv.imshow('threshold inverse', thresh_inv)

#Adaptative threshold
adaptative_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptative threshold', adaptative_thresh)

cv.waitKey(0)