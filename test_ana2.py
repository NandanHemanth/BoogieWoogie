# import cv2
# import mediapipe as mp
# import time
# import math
# import csv

# # Initializing Mediapipe Pose framework
# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()

# # Initialize variables
# pTime = 0
# frame_num = 0
# prev_cx, prev_cy = None, None

# # Open a CSV file to save the distances
# with open('Real_time.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Frame", "Landmark ID", "cx", "cy", "Euclidean Distance"])

#     # Start video capture
#     cap = cv2.VideoCapture(0)

#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         frame_num += 1
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = pose.process(imgRGB)
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

#         if results.pose_landmarks and frame_num % 8 == 0:
#             for id, lm in enumerate(results.pose_landmarks.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)

#                 if prev_cx is not None and prev_cy is not None:
#                     # Calculate Euclidean distance
#                     distance = math.sqrt((cx - prev_cx) ** 2 + (cy - prev_cy) ** 2)
#                 else:
#                     distance = 0  # No previous point, so distance is 0

#                 # Write to CSV
#                 writer.writerow([frame_num, id, cx, cy, distance])

#                 # Update previous coordinates
#                 prev_cx, prev_cy = cx, cy

#         # Calculate and display FPS
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime

#         cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#         cv2.imshow("Image", img)

#         # Exit loop if ESC is pressed
#         if cv2.waitKey(2) & 0xFF == 27:
#             break

# cap.release()
# cv2.destroyAllWindows()

###############################

import cv2
import mediapipe as mp
import time
import math
import csv

# Initializing Mediapipe Pose framework
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Initialize variables
pTime = 0
frame_num = 0
prev_cx, prev_cy = None, None

# Open a CSV file to save the distances
with open('real_dance.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "Landmark ID", "cx", "cy", "Euclidean Distance"])

    # Start video capture
    cap = cv2.VideoCapture(0)

    # Set the duration limit to 200 seconds
    capture_duration = 200  # This will capture for 200 seconds

    # Record the start time
    start_time = time.time()

    while True:
        success, img = cap.read()
        if not success:
            break

        frame_num += 1
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

            if frame_num % 8 == 0:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    if prev_cx is not None and prev_cy is not None:
                        # Calculate Euclidean distance
                        distance = math.sqrt((cx - prev_cx) ** 2 + (cy - prev_cy) ** 2)
                    else:
                        distance = 0  # No previous point, so distance is 0

                    # Write to CSV
                    writer.writerow([frame_num, id, cx, cy, distance])

                    # Update previous coordinates
                    prev_cx, prev_cy = cx, cy

        # Calculate and display FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)

        # Check if the capture duration has exceeded 200 seconds
        elapsed_time = time.time() - start_time
        if elapsed_time > capture_duration:
            print("200 seconds have passed. Stopping capture.")
            break

        # Exit loop if ESC is pressed
        if cv2.waitKey(2) & 0xFF == 27:
            print("ESC pressed, exiting.")
            break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
