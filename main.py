import cv2
from face_tracker import FaceTracker
from utils import initialize_video_capture, cleanup_resources
import logging

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting facial tracking application")
    tracker = FaceTracker()
    cap = initialize_video_capture()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                logger.warning("Failed to read frame from video capture")
                break
                
            processed_frame, coordinates = tracker.process_frame(frame)
            
            # Log coordinates for debugging
            logger.debug(f"Coordinates: nose_tip={coordinates.nose_tip}, "
                        f"left_eye={coordinates.left_eye}, "
                        f"right_eye={coordinates.right_eye}, "
                        f"mouth_center={coordinates.mouth_center}")
            
            # Overlay text on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            color = (255, 255, 255)  # White text
            thickness = 1
            line_spacing = 20
            y_offset = 20  # Starting y position from top

            # List of text lines to display
            text_lines = [
                f"Nose Tip: {coordinates.nose_tip}",
                f"Left Eye: {coordinates.left_eye}",
                f"Right Eye: {coordinates.right_eye}",
                f"Mouth Center: {coordinates.mouth_center}",
                f"Mouth Width: {coordinates.mouth_width:.2f}",
                f"Left Eye Blink: {coordinates.eye_blink_left:.2f}",
                f"Right Eye Blink: {coordinates.eye_blink_right:.2f}",
                f"Head Rotation: {coordinates.head_rotation}"
            ]

            # Draw each line of text
            for i, line in enumerate(text_lines):
                y_pos = y_offset + (i * line_spacing)
                cv2.putText(
                    processed_frame, 
                    line, 
                    (10, y_pos),  # Position (x, y)
                    font, 
                    font_scale, 
                    color, 
                    thickness, 
                    cv2.LINE_AA
                )
            
            # Display the frame with text
            cv2.imshow('Facial Tracking', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logger.info("User requested shutdown with 'q' key")
                break
                
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        
    finally:
        cleanup_resources(cap, tracker.face_mesh)
        logger.info("Application shutdown complete")

if __name__ == "__main__":
    main()