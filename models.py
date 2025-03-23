from dataclasses import dataclass

@dataclass
class FaceCoordinates:
    """Data structure for facial feature coordinates and metrics."""
    nose_tip: tuple = (0, 0)
    left_eye: tuple = (0, 0)
    right_eye: tuple = (0, 0)
    mouth_center: tuple = (0, 0)
    mouth_width: float = 0.0
    eye_blink_left: float = 0.0
    eye_blink_right: float = 0.0
    head_rotation: tuple = (0.0, 0.0, 0.0)  # x, y, z