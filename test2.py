import cv2
from picamera2 import Picamera2,Preview

from ultralytics import YOLO

cam = Picamera2()     
camera_config = cam.create_preview_configuration(main={'format':'RGB888'})
cam.configure(camera_config)
cam.start()

model = YOLO('yolov8n.pt')

while True:
    try:
        image = cam.capture_array()
        results = model(image)
        # Process the image using OpenCV
        cv2.imshow("Frame", image)

        for result in results:
            boxes = result.boxes
            probs = result.probs

        if cv2.waitKey(1) == ord("q"):
            break
    except Exception as e:
        print(f"Error: {e}")
        break

cam.stop_preview()
cv2.destroyAllWindows()
