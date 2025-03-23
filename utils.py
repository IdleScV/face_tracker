import cv2
import socket
import json

def initialize_video_capture(device_id=0):
    cap = cv2.VideoCapture(device_id)
    if not cap.isOpened():
        raise Exception("Error: Could not open webcam.")
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