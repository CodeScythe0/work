from picamera2 import Picamera2
import cv2
from ultralytics import YOLO

cam = Picamera2()     
camera_config = cam.create_preview_configuration(main={'format':'RGB888'})
cam.configure(camera_config)
cam.start()

model = YOLO('yolov8n.pt')

# Loop through the video frames
while True:
    image = cam.capture_array()
    # Run YOLOv8 inference on the frame
    results = model(image)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture object and close the display window
cv2.destroyAllWindows()