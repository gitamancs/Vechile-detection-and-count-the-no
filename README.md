# Vehicle Tracking using OpenCV

This project demonstrates Vehicle tracking using OpenCV, a popular computer vision library. The implementation involves detecting and tracking Vehicles in a video stream, applying background subtraction, and utilizing the Euclidean Distance Tracker.
It employs a combination of Vehicle detection and tracking techniques to follow Vehicle in a defined region of interest (ROI).

## Table of Contents
- [Usage](#usage)
- [Components](#components)
- [Dependencies](#Dependencies)
- [Configuration](#configuration)
- [Acknowledgement](#acknowledgements)
- [Future Enhancement](#futureenhancement)
- [Note](#note)
- [License](#license)
## Overview

## Usage

1. Install OpenCV:

   ```bash
   pip install opencv-python
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/object-tracking.git
   cd object-tracking
   ```

3. Run the script:

   ```bash
   python Detect object and count.py
   ```

## Components

The main components of the project include:

1. **Vehicle Detection:** The project uses a background subtraction technique to detect moving Vehicle within a specified ROI. The MOG2 background subtractor is applied to identify changes in the scene.

2. **Vehicle Tracking:** Vehicle tracking is achieved using the Euclidean Distance Tracker. This tracker assigns unique IDs to detected Vehicles and maintains continuity as they move through the frames.

3. **Processing Frames:** The process_frame function processes each frame of the video, applies Vehicle detection, and performs Vehicle tracking. The resulting frame is then displayed, showing tracked Vehicle and their assigned IDs.

4. **Displaying FPS:** The frames per second (FPS) are calculated and displayed on the original frame to provide information about the processing speed.

## Dependencies

- OpenCV

## Configuration

- Input Video: Modify the `cap = cv2.VideoCapture(...)` line to specify the path to your input video.

## Acknowledgments

- [OpenCV Documentation](https://docs.opencv.org/)
- Tracker implementation inspired by [PyImageSearch](https://www.pyimagesearch.com/)

## Future Enhancements
Possible future enhancements include integrating more advanced Vehicle detection models and exploring multi-Vehicle tracking strategies for improved performance.

## Note
  Make sure to replace the video file path and add any additional details specific to your implementation before including this project description in your resume.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
