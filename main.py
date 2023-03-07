#!/usr/bin/env python3
import cv2 as cv
import numpy as np

ogimage = cv.imread('coyote.jpg')
ogimage = ogimage[:710, :]
image = cv.cvtColor(ogimage, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(image, 128, 255, 0)
conts, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cont_image = cv.drawContours(np.zeros(ogimage.shape), conts, -1, (0,255,0))
cv.imshow('coyote', cont_image)

while cv.waitKey(0) != ord('q'):
    pass
