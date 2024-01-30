import cv2
from picamera2 import Picamera2,Preview

cam = Picamera2()     
camera_config = cam.create_preview_configuration(main={'format': 'RGB888','size':(3840,2160)})
cam.configure(camera_config)
cam.start()

while True:
    try:
        image = cam.capture_array()

        # Process the image using OpenCV
        cv2.imshow("Frame", image)

        if cv2.waitKey(1) == ord("q"):
            break
    except Exception as e:
        print(f"Error: {e}")
        break

cam.stop_preview()
cv2.destroyAllWindows()
