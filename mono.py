import cv2
import numpy as np
import mediapipe as mp

# Initialize mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

def calculate_angle(point1, point2, point3):
    """Calculate the angle between three points."""
    a = np.array(point1)
    b = np.array(point2)
    c = np.array(point3)
    ab = a - b
    cb = c - b
    cosine_angle = np.dot(ab, cb) / (np.linalg.norm(ab) * np.linalg.norm(cb))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def draw_text(frame, text, pos, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, font_thickness=2):
    """Draws a semi-transparent text box with styled text."""
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    box_x, box_y = pos
    box_w, box_h = text_size[0] + 20, text_size[1] + 20

    # Draw a semi-transparent box for the text
    overlay = frame.copy()
    cv2.rectangle(overlay, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)

    # Add the text on top of the box
    text_x = box_x + 10
    text_y = box_y + box_h - 10
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 255, 255), font_thickness + 1, cv2.LINE_AA)
    return frame

def monitor_face_position():
    # Initialize Video Capture
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB for mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                
                # Map important landmarks to 2D coordinates
                landmarks = [
                    (int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in [1, 33, 263, 61, 291, 199]
                ]
                
                # Calculate angles based on face orientation
                angle_left = calculate_angle(landmarks[0], landmarks[1], landmarks[3])
                angle_right = calculate_angle(landmarks[0], landmarks[2], landmarks[4])
                
                # Check deviation threshold (35 degrees)
                if angle_left > 35 or angle_right > 35:
                    frame = draw_text(frame, "Look at the Screen", (50, 50), font_scale=1.2, font_thickness=2)

                # Draw boxes around landmarks
                for x, y in landmarks:
                    cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 255, 0), -1)

        # Display the frame with the enhanced visuals
        cv2.imshow('Face Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the face position monitor
monitor_face_position()
