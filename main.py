import cv2
from face_tracker import FaceTracker
from utils import initialize_video_capture, cleanup_resources, initialize_socket, send_coordinates

def main():
    tracker = FaceTracker()
    cap = initialize_video_capture()
    sock = initialize_socket()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            processed_frame, coordinates = tracker.process_frame(frame)
            send_coordinates(sock, coordinates)
            
            # Optional: Display locally
            cv2.imshow('Facial Tracking', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        cleanup_resources(cap, tracker.face_mesh, sock)

if __name__ == "__main__":
    main()