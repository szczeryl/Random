import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Function to compute angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return 180.0 - np.degrees(angle)

# Set up webcam (external = 1, built-in = 0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert color and process
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        # Back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        h, w, _ = image.shape

        try:
            landmarks = results.pose_landmarks.landmark

            def to_pixel(landmark):
                return np.array([landmark.x * w, landmark.y * h])

            # Get shoulders and hips
            l_shoulder = to_pixel(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER])
            r_shoulder = to_pixel(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER])
            l_hip = to_pixel(landmarks[mp_pose.PoseLandmark.LEFT_HIP])
            r_hip = to_pixel(landmarks[mp_pose.PoseLandmark.RIGHT_HIP])

            # Midpoints
            top = (l_shoulder + r_shoulder) / 2
            bottom = (l_hip + r_hip) / 2
            middle = (top + bottom) / 2

            # Cobb-like angle (at middle point)
            cobb_angle = calculate_angle(top, middle, bottom)

            # Draw working lines
            cv2.line(image, tuple(top.astype(int)), tuple(middle.astype(int)), (0, 255, 255), 3)
            cv2.line(image, tuple(middle.astype(int)), tuple(bottom.astype(int)), (0, 255, 255), 3)

            # Draw angle text
            cv2.putText(image, f"Estimated Cobb Angle: {int(cobb_angle)} deg",
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                        (0, 255, 0) if cobb_angle <= 10 else (0, 0, 255), 3)

            # Optional alert
            if cobb_angle > 10:
                cv2.putText(image, "Poor Posture Detected!", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        except Exception as e:
            pass

        # Draw landmarks (simplified dots)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(200, 200, 200), thickness=1, circle_radius=1),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(100, 255, 100), thickness=2)
        )

        # Display
        cv2.imshow("Cobb Angle Estimator", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
