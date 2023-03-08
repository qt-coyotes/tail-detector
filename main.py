#!/usr/bin/env python3
# https://docs.opencv.org/4.7.0/db/d28/tutorial_cascade_classifier.html
# https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf
import cv2 as cv
import numpy as np

ogimage = cv.imread('coyote.jpg')
ogimage = ogimage[:710, :]

kernel = np.ones((5,5), np.float32)
kernel /= kernel.size
image = cv.filter2D(ogimage, -1, kernel)
cv.imshow('blurr_coyote', image)

image = cv.cvtColor(ogimage, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(image, 128, 255, 0)
conts, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cont_image = cv.drawContours(np.zeros(ogimage.shape), conts, -1, (0,255,0))
cv.imshow('coyote', cont_image)

while cv.waitKey(0) != ord('q'):
    pass
