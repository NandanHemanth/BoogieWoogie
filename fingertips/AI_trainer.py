# import cv2
# import numpy as np
# import mediapipe as mp
# import time

# # initialising framework
# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()

# pTime = 0

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)
#     # print(results.pose_landmarks)

#     lmList = []

#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

#         for id, lm in enumerate(results.pose_landmarks.landmark):
#             h, w, c = img.shape
#             # print(id, lm)
#             cx, cy = int(lm.x*w), int(lm.y*h)
#             lmList.append([id, cx, cy])
#             # print(lmList)

#             if len(lmList) != 0:
#                 # findAngle here
#             # cv2.circle(img, (cx, cy), 3, (255,0,0), cv2.FILLED)

        
#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime

#     cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
#                 (255, 0, 0), 3)
#     cv2.imshow("Image", img)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break

##############

import cv2
import numpy as np
import mediapipe as mp
import time
import math

# Define findAngle function
def findAngle(img, lmList, p1, p2, p3, draw=True):
    # Get the landmarks
    x1, y1 = lmList[p1][1:]
    x2, y2 = lmList[p2][1:]
    x3, y3 = lmList[p3][1:]
    
    # Calculate the Angle
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    
    # Draw
    if draw:
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
        cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
        cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
        cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
        cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    
    return angle

# Initializing framework
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

pTime = 0
dir = 0
count = 0

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    lmList = []

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])

        if len(lmList) != 0:
            # Example: Calculate the angle between shoulder, elbow, and wrist
            # p1 (shoulder), p2 (elbow), p3 (wrist)
            # Using indices of specific landmarks in the pose model
            shoulder = 11  # Left Shoulder
            elbow = 13     # Left Elbow
            wrist = 15     # Left Wrist
            
            # Find the angle between shoulder, elbow, and wrist
            angle = findAngle(img, lmList, shoulder, elbow, wrist)
            per = np.interp(angle,(60, 160), (100,0))
            print(angle, per)

            if per==100:
                if dir == 0:
                    count += 0.5
                    print(count)
                    dir = 1
            if per==0:
                if dir == 1:
                    count += 0.5
                    print(count)
                    dir = 0

    # Calculate and display the FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(count), (500,75), cv2.FONT_HERSHEY_PLAIN, 5,
                (255,0,0), 5)
    # cv2.rectangle(img,(0,450), (250, 720), (0,255,0),cv2.FILLED)

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
 