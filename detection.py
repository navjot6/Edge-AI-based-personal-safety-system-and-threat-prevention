import cv2
import mediapipe as mp
import numpy as np
from alert import send_alert

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

THRESHOLD = 0.7

def detect_threat():
    cap = cv2.VideoCapture(0)
    risk_score = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark
            
            left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
            nose = landmarks[mp_pose.PoseLandmark.NOSE.value].y

            # Simple distress logic
            if left_wrist < nose or right_wrist < nose:
                risk_score += 0.1
            else:
                risk_score -= 0.05

        risk_score = max(0, min(risk_score, 1))

        cv2.putText(frame, f"Risk Score: {round(risk_score,2)}",
                    (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        if risk_score > THRESHOLD:
            send_alert("Threat detected! Immediate attention required.")
            risk_score = 0

        cv2.imshow("Women Safety Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
