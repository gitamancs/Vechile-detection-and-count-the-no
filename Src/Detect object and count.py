import cv2
from tracker import EuclideanDistTracker

def process_frame(frame, object_detector, tracker):
    height, width, _ = frame.shape
    roi = frame[280:720, 350:800]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Object Tracking
    boxes_ids = tracker.update(detections)

    for box_id in boxes_ids:
        x, y, w, h, track_id = box_id
        cv2.putText(roi, str(track_id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    return roi

def main():
    tracker = EuclideanDistTracker()
    cap = cv2.VideoCapture(r'D:\My Prog\Naresh_i _Technology\1_Downloads\Computer Vision\object_tracking\highway.mp4')
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        processed_frame = process_frame(frame, object_detector, tracker)

        # Display FPS
        fps = cap.get(cv2.CAP_PROP_FPS)
        cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Processed Frame", processed_frame)
        cv2.imshow("Original Frame", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
