import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)

#paint image certain color
# blank[200:300,300:400] = 255,255,255

#rectangle
cv.rectangle(blank, (0,0), (blank.shape[0]//2 ,blank.shape[1]//2) , (0,255,0) ,thickness=cv.FILLED)
cv.imshow('Green',blank)
cv.waitKey(0)