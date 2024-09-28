# importing libraries
import cv2
import mediapipe as mp 
import numpy as np

# initialize mediapipe pose detection
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Video feed real-time
cap = cv2.VideoCapture(10)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Video Feed', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
