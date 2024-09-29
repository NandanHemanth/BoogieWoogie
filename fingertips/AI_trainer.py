import cv2
import numpy as np
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break