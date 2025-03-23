import cv2
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("facial_tracking.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
logger.info("Loaded .env file")

def load_config():
    """Load configuration from environment variables."""
    return {
        "VIDEO_CAPTURE_DEVICE": int(os.getenv("VIDEO_CAPTURE_DEVICE", 0)),
        "SHOW_LANDMARKS": os.getenv("SHOW_LANDMARKS", "False").lower() == "true",
        "SHOW_OVERLAY": os.getenv("SHOW_OVERLAY", "True").lower() == "true",
        "LOG_FRAME_INTERVAL": int(os.getenv("LOG_FRAME_INTERVAL", 10)),
    }

def initialize_video_capture():
    """Initialize video capture device with fallback.

    Returns:
        OpenCV VideoCapture object.
    Raises:
        Exception: If no video device is available.
    """
    config = load_config()
    device_id = config["VIDEO_CAPTURE_DEVICE"]
    logger.info(f"Initializing video capture with device ID: {device_id}")
    cap = cv2.VideoCapture(device_id)

    if not cap.isOpened():
        logger.warning(f"Device {device_id} failed, trying default device 0")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            logger.error("No video device available")
            raise Exception("Error: No video device available")

    logger.info("Video capture initialized successfully")
    return cap

def cleanup_resources(cap, face_mesh):
    """Clean up video capture and FaceMesh resources.

    Args:
        cap: OpenCV VideoCapture object.
        face_mesh: MediaPipe FaceMesh object.
    """
    logger.info("Cleaning up resources")
    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()
    logger.info("Resources cleaned up")