from imutils import contours
import numpy as np
import imutils
import cv2
import csv

image = cv2.imread('test_image.png')
cv2.imshow("original image", image)
cv2.waitKey(0)    
