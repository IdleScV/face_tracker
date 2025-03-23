# Project Progress Tracker

This Markdown file tracks the progress of building a Python face tracking tool for live movements in Blender, specifically using shape keys to drive facial animations. Each task is listed as a ticket with a checkbox to mark completion. Use this to stay organized and ensure all steps are completed systematically.

---

## Tickets

### 1. Research and Select a Python Library for Real-Time Face Tracking

- [x] Evaluate Python libraries such as OpenCV, Dlib, and MediaPipe for real-time face tracking.
- [x] Focus on accuracy, performance, and the ability to extract detailed facial feature data (e.g., key points for eyes, mouth, and eyebrows) suitable for shape key control.
- **Purpose**: Select a reliable library as the foundation for the face tracking system.

### 2. Implement Basic Face Tracking with Visualization

- [x] Set up webcam capture using the chosen library.
- [x] Detect facial key points in real-time.
- [x] Add visualization (e.g., overlay key points on the video feed) to confirm tracking accuracy.
- **Purpose**: Establish core functionality for capturing and processing facial data.

### 3. Identify and Extract Relevant Facial Feature Data for Shape Keys

- [ ] Determine which facial features (e.g., eye positions, mouth shape, eyebrow movement) correspond to the shape keys in the Blender model.
- [ ] Extract these specific data points from the tracking output and process them into normalized values (0 to 1) suitable for shape key activation.
- **Purpose**: Ensure the right data is captured and prepared for driving shape keys in Blender.

### 4. Research and Implement Real-Time Data Transmission from Python to Blender

- [ ] Investigate methods for sending data from Python to Blender in real-time (e.g., OSC protocol, sockets).
- [ ] Implement the most suitable approach for real-time data transfer, ensuring the data format supports shape key values.
- **Purpose**: Enable live communication between the Python tool and Blender.

### 5. Set Up Data Reception and Mapping to Shape Keys in Blender

- [ ] Use Blender’s Python API to receive the transmitted facial data.
- [ ] Map the received normalized values to the corresponding shape keys in the Blender model (e.g., linking mouth width value to the 'mouth_open' shape key).
- **Purpose**: Bridge the gap between the Python tool and Blender for live animation using shape keys.

### 6. Test and Debug the Entire Pipeline

- [ ] Test the full system from video capture to Blender animation via shape keys.
- [ ] Debug issues related to latency, accuracy, or stability.
- **Purpose**: Ensure the system works reliably in real-time.

### 7. Optimize for Performance

- [ ] Profile the application to identify bottlenecks (e.g., slow tracking, data transmission, or shape key updates).
- [ ] Implement optimizations to reduce latency and increase frame rates.
- **Purpose**: Achieve smooth, live animations without noticeable delays.

### 8. (Optional) Develop a Simple GUI

- [ ] Create a basic graphical user interface (e.g., with buttons to start/stop tracking or calibrate the system).
- **Purpose**: Improve usability, especially for future expansions or sharing the tool.

---

## Additional Notes or Tasks

- [ ] Set up a Git repository for version control.
- [ ] Document progress and decisions in a README or code comments.
- [ ] Implement a calibration step to normalize facial feature data for different users, ensuring consistent mapping to shape keys.
- [ ] (Optional) Add a recording feature for tracking data for later use.

---

**Tips**:

- Complete tickets in order for a smooth workflow.
- Use the checkboxes to track your progress (e.g., change `[ ]` to `[x]` when done).
- Add any new tasks or notes in the "Additional Notes or Tasks" section as needed.

---

### Key Updates Made:

1. **Ticket 3**: Specified that facial feature data should be processed into normalized values (0 to 1) for shape keys, aligning with Blender’s requirements.
2. **Ticket 5**: Clarified that mapping is specifically to shape keys (removed mention of rigs to focus on your stated goal) and provided an example for clarity.
3. **Additional Notes**: Updated the optional calibration task to focus on normalizing data for different users, which enhances shape key consistency.
4. **General**: Adjusted wording throughout to emphasize the use of shape keys, ensuring the tracker reflects your intent to connect the face tracking tool to Blender via shape keys.

This updated tracker should guide you effectively toward building a Python face tracking tool that drives Blender animations using shape keys in real-time. Let me know if you need further tweaks!
