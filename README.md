# Facial Tracking Project

This project implements a real-time facial tracking system using OpenCV, MediaPipe, and Python. It captures video from a webcam, detects facial landmarks, and displays them overlayed on the video feed. The system is designed to be modular and extensible, with plans to integrate with a Blender facial rig in future iterations.

## Features

- Real-time facial landmark detection using MediaPipe's Face Mesh
- Tracks key facial features: nose tip, left eye, right eye, and mouth center
- Displays tracked points on a live video feed
- Configurable video capture device via a `.env` file
- Comprehensive logging for debugging and verification
- Modular codebase split into multiple files for maintainability

## Requirements

- Python 3.7+

## Installation

1. **Clone the Repository** (if using Git):

   ```bash
   git clone <repository-url>
   cd facial_tracking
   ```

   If not using Git, simply create a directory and place the files there.

2. **Set Up a Virtual Environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```
     VIDEO_CAPTURE_DEVICE=0  # Replace with your webcam device ID (e.g., 0, 1, 2)
     ```
   - Adjust the `VIDEO_CAPTURE_DEVICE` value based on your system's webcam index.

## Project Structure

```
facial_tracking/
├── .env                # Environment variables (not tracked by Git)
├── .gitignore          # Git ignore file
├── main.py             # Entry point for the application
├── face_tracker.py     # Facial tracking logic
├── models.py           # Data classes for coordinates
├── utils.py            # Utility functions (video capture, logging)
├── requirements.txt    # Dependency list
├── facial_tracking.log # Log file (generated on run)
```

## Usage

1. **Activate the Virtual Environment** (if used):

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Application**:

   ```bash
   python main.py
   ```

3. **What to Expect**:

   - A window will open showing your webcam feed with green facial mesh and colored dots on key points (red for nose, blue for eyes, yellow for mouth).
   - Logs will be written to `facial_tracking.log` and displayed in the console.
   - Press 'q' to quit the application.

4. **Sample Log Output**:
   ```
   2025-03-22 22:50:33,304 - INFO - Loaded .env file
   2025-03-22 22:50:33,305 - INFO - Starting facial tracking application
   2025-03-22 22:50:33,312 - INFO - Initializing video capture with device ID: 0
   2025-03-22 22:50:33,629 - INFO - Video capture initialized successfully
   ```

## Current Status

- The application successfully captures video and tracks facial landmarks in real-time.
- Socket communication to Blender is not currently implemented (removed temporarily to focus on core tracking functionality).
- Future enhancements will include:
  - Reintegrating socket communication for Blender integration
  - Adding more facial features (mouth width, eye blinks, head rotation)
  - Improving performance and smoothing of tracked points

## Troubleshooting

- **No Video Feed**:
  - Verify the `VIDEO_CAPTURE_DEVICE` in `.env` matches your webcam's device ID.
  - Test with different values (0, 1, 2, etc.).
- **No Landmarks**:
  - Ensure your face is visible to the camera and well-lit.
- **Errors**:
  - Check `facial_tracking.log` for detailed error messages.
- **Dependency Issues**:
  - Ensure the virtual environment is active and `requirements.txt` was installed correctly.

## Contributing

Feel free to fork this project and submit pull requests with improvements. Current areas for enhancement include:

- Adding socket support for Blender integration
- Implementing additional facial feature tracking
- Optimizing performance

## License

This project is unlicensed for now. Feel free to use and modify it as needed.

---

### Benefits of This Approach

1. **Single Command**: `pip install -r requirements.txt` installs everything at once.
2. **Version Control**: Specific versions ensure compatibility across systems.
3. **Virtual Environment**: Encourages isolated environments, preventing conflicts with other projects.
4. **Reproducibility**: Anyone can set up the exact same environment easily.

### Updated Directory Structure

```
facial_tracking/
├── .env
├── .gitignore
├── main.py
├── face_tracker.py
├── models.py
├── utils.py
├── requirements.txt    # New file
├── facial_tracking.log
```
