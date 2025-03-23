import cv2
import mediapipe as mp
import numpy as np
from models import FaceCoordinates

class FaceTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
        # Calibration values
        self.mouth_width_base = None
        self.eye_blink_base_left = None
        self.eye_blink_base_right = None

    def calculate_features(self, landmarks, h, w):
        # Convert landmarks to pixel coordinates
        def to_pixel(landmark_idx):
            return (int(landmarks.landmark[landmark_idx].x * w),
                    int(landmarks.landmark[landmark_idx].y * h))

        coordinates = FaceCoordinates()
        
        # Basic coordinates
        coordinates.nose_tip = to_pixel(1)
        coordinates.left_eye = to_pixel(33)
        coordinates.right_eye = to_pixel(263)
        coordinates.mouth_center = to_pixel(0)
        
        # Mouth width (distance between mouth corners)
        mouth_left = to_pixel(61)
        mouth_right = to_pixel(291)
        coordinates.mouth_width = np.linalg.norm(np.array(mouth_right) - np.array(mouth_left))
        
        # Eye blink (distance between upper and lower eyelids)
        left_eye_top = to_pixel(159)
        left_eye_bottom = to_pixel(145)
        right_eye_top = to_pixel(386)
        right_eye_bottom = to_pixel(374)
        
        coordinates.eye_blink_left = np.linalg.norm(np.array(left_eye_top) - np.array(left_eye_bottom))
        coordinates.eye_blink_right = np.linalg.norm(np.array(right_eye_top) - np.array(right_eye_bottom))
        
        # Head rotation (simplified, using nose tip and eye positions)
        eye_center = ((coordinates.left_eye[0] + coordinates.right_eye[0]) / 2,
                      (coordinates.left_eye[1] + coordinates.right_eye[1]) / 2)
        nose_vec = np.array(coordinates.nose_tip) - np.array(eye_center)
        coordinates.head_rotation = (nose_vec[1] / h, nose_vec[0] / w, 0.0)  # Simple approximation
        
        # Normalize values (after first frame calibration)
        if self.mouth_width_base is None:
            self.mouth_width_base = coordinates.mouth_width
            self.eye_blink_base_left = coordinates.eye_blink_left
            self.eye_blink_base_right = coordinates.eye_blink_right
        
        coordinates.mouth_width = (coordinates.mouth_width / self.mouth_width_base) - 1.0
        coordinates.eye_blink_left = 1.0 - (coordinates.eye_blink_left / self.eye_blink_base_left)
        coordinates.eye_blink_right = 1.0 - (coordinates.eye_blink_right / self.eye_blink_base_right)
        
        return coordinates

    def process_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        coordinates = FaceCoordinates()
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mp_drawing.DrawingSpec(
                        color=(0, 255, 0),
                        thickness=1,
                        circle_radius=1
                    )
                )
                h, w = frame.shape[:2]
                coordinates = self.calculate_features(face_landmarks, h, w)
                
                # Draw key points
                cv2.circle(frame, coordinates.nose_tip, 5, (0, 0, 255), -1)
                cv2.circle(frame, coordinates.left_eye, 5, (255, 0, 0), -1)
                cv2.circle(frame, coordinates.right_eye, 5, (255, 0, 0), -1)
                cv2.circle(frame, coordinates.mouth_center, 5, (0, 255, 255), -1)
        
        return frame, coordinates