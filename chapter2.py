#!/usr/bin/python3
# chapter 2 - basic functions
import cv2
import numpy as np

# turning image to grayscale

img = cv2.imread("images/lenna.png")
kernel = np.ones((5,5), np.uint8)

# opencv convention is BGR not RGB
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# how to turn the image blurry
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# Edge Detector
imgCanny = cv2.Canny(img, 150, 200)
# how to increase the thickness of the edges
# higher the iterations, the thicker the line, etc
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# how to make the lines thiner
imgEroded = cv2.erode(imgDialation, kernel, iterations =1)

# "image title", image_file 
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Image Dialation", imgDialation)
cv2.imshow("Image Eroded", imgEroded)
cv2.waitKey(0)
