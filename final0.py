from picamera2 import Picamera2, Preview
import cv2
import time
from ultralytics import YOLO
import os

cam = Picamera2()
camera_config = cam.create_preview_configuration(main={'format': 'RGB888','size':(3280,2464)})
cam.configure(camera_config)
cam.start()

model = YOLO('yolov8n.onnx',task='detect')

cv2.namedWindow("Inference", cv2.WINDOW_NORMAL)

# Loop through the video frames
while True:
    start_time = time.time()  # Start time measurement before inference

    image = cam.capture_array()

    results = next(model(image, stream=True, imgsz=256))

    inference_time = time.time() - start_time  # Calculate inference time
    
    annotated_frame = results.plot()

    objs = ''
    for r in results:
        obj = r.names[int(r.boxes.cls[0].item())]
        cord = r.boxes.xyxy.tolist()[0]
        objs = objs + obj + ' '
        print(cord)

    os.system('echo "{0}" | festival --tts'.format(objs)) 

    cv2.imshow("Inference", annotated_frame)

    #print("fps:", 1/inference_time)  # Print the inference time
    #cv2.imshow("Inference", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
