#!/usr/bin/python3
# chapter 1 - images / videos/ webcam
import cv2

# How to show an image ---------------------------------------------------------
img = cv2.imread("images/lenna.png")
# Syntax: cv2.imshow(window_name, image)
# Parameters:
# window_name: A string representing the name of the window in which image to be displayed.
# image: It is the image that is to be displayed.
# Return Value: It doesn’t returns anything.+
cv2.imshow("Output", img)
# if you exit the image, your command prompt will freeze
# setting waitKey to 0 will make it wait forever or untill pressed
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(1)


# how to play a video ----------------------------------------------------------
capture = cv2.VideoCapture("images/fast_moving_move_base.mp4")
while True:
    sucess, vid = capture.read()
    cv2.imshow("Video", vid)
    # pressing the button q will exit/break the video
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Webcam -----------------------------------------------------------------------
capture = cv2.VideoCapture(0)
# how to change the size of the video capture (3=width, 4 =height)
capture.set(3, 640)
capture.set(4, 480)
# sets the brightness
capture.set(10, 100)

while True:
    sucess, vid = capture.read()
    cv2.imshow("Webcam", vid)
    # pressing the button q will exit/break the video
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#closing all open windows
cv2.destroyAllWindows()
