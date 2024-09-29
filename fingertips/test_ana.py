# import cv2
# import mediapipe as mp
# import time
# import numpy as np
# import pandas as pd
# from datetime import datetime

# # Initialize MediaPipe Pose and drawing utilities
# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()

# pTime = 0

# # Initialize video capture
# cap = cv2.VideoCapture('./JD_americano.mp4')

# # List to store scores
# scores_list = []

# # Example reference points for IDs 12, 13, 25, 26 (you should adjust these)
# reference_pose = {
#     12: (0.5, 0.5),  # Replace with actual reference coordinates
#     13: (0.5, 0.6),
#     25: (0.5, 0.8),
#     26: (0.5, 0.9),
# }

# def calculate_score(landmarks, h, w):
#     distance_sum = 0
#     for id in reference_pose:
#         ref_point = reference_pose[id]
#         current_point = (landmarks[id].x * w, landmarks[id].y * h)
#         distance = np.linalg.norm(np.array(ref_point) - np.array(current_point))
#         distance_sum += distance
    
#     # Normalize to a score out of 100
#     max_distance_sum = 1000  # Adjust this value as needed
#     score = 100 - (distance_sum / max_distance_sum * 100)
#     score = max(0, min(100, score))  # Ensure score is between 0 and 100
#     return score

# while True:
#     success, img = cap.read()
#     if not success:
#         break
    
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
#         # Get image dimensions
#         h, w, c = img.shape
        
#         # Calculate score for the tracked landmarks
#         score = calculate_score(results.pose_landmarks.landmark, h, w)
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         scores_list.append({'Timestamp': timestamp, 'Score': score})

#         # Display score on the image
#         cv2.putText(img, f'Score: {int(score)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

#     # Display FPS on the image
#     cTime = time.time()
#     fps = 1/(cTime - pTime)
#     pTime = cTime
#     cv2.putText(img, f'FPS: {int(fps)}', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

#     # Show the image
#     cv2.imshow("Image", img)

#     # Break the loop on 'ESC' key press
#     if cv2.waitKey(2) & 0xFF == 27:
#         break

# # Save scores to a CSV file after video processing
# df = pd.DataFrame(scores_list)
# df.to_csv('dance_scores.csv', index=False)

# print("Scores saved to dance_scores.csv")

# # Release the video capture and destroy all windows
# cap.release()
# cv2.destroyAllWindows()

###########################################################

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
with open('just_dance.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "Landmark ID", "cx", "cy", "Euclidean Distance"])

    # Start video capture
    cap = cv2.VideoCapture('./JD_americano.mp4')

    while True:
        success, img = cap.read()
        if not success:
            break

        frame_num += 1
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)

        if results.pose_landmarks and frame_num % 8 == 0:
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

        # Exit loop if ESC is pressed
        if cv2.waitKey(2) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

