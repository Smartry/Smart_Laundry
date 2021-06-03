import sys
import cv2
img = cv2.imread('blue-whale.png' ,0)
cv2.imshow('image', img)
cv2.waitKey(0)