# importing libraries
import cv2
import mediapipe as mp
import time
import numpy

cap = cv2.VideoCapture("/video1.mp4")

prev_time = 0

while True:
    success, img = cap.read()

    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

