import cv2
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('facial_tracking.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
logger.info("Loaded .env file")

def initialize_video_capture():
    device_id = int(os.getenv("VIDEO_CAPTURE_DEVICE", 0))
    logger.info(f"Initializing video capture with device ID: {device_id}")
    cap = cv2.VideoCapture(device_id)
    if not cap.isOpened():
        logger.error(f"Failed to open webcam with device ID {device_id}")
        raise Exception(f"Error: Could not open webcam with device ID {device_id}.")
    logger.info("Video capture initialized successfully")
    return cap

def cleanup_resources(cap, face_mesh):
    logger.info("Cleaning up resources")
    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()
    logger.info("Resources cleaned up")