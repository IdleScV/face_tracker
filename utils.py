import cv2
import socket
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def initialize_video_capture():
    # Get device ID from environment variable, default to 0 if not set
    device_id = int(os.getenv("VIDEO_CAPTURE_DEVICE", 0))
    cap = cv2.VideoCapture(device_id)
    if not cap.isOpened():
        raise Exception(f"Error: Could not open webcam with device ID {device_id}.")
    return cap

def cleanup_resources(cap, face_mesh, sock=None):
    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()
    if sock:
        sock.close()

def initialize_socket(host='localhost', port=5000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def send_coordinates(sock, coordinates):
    data = {
        'nose_tip': coordinates.nose_tip,
        'left_eye': coordinates.left_eye,
        'right_eye': coordinates.right_eye,
        'mouth_center': coordinates.mouth_center,
        'mouth_width': coordinates.mouth_width,
        'eye_blink_left': coordinates.eye_blink_left,
        'eye_blink_right': coordinates.eye_blink_right,
        'head_rotation': coordinates.head_rotation
    }
    sock.send(json.dumps(data).encode('utf-8'))