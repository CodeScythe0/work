#!/usr/bin/env python3

#  Dependencies
import time
import os

from ultralytics import YOLO
from picamera2 import Picamera2, Preview
import cv2
import pyfirmata2

# Setup
cam = Picamera2()
camera_config = cam.create_preview_configuration(main={'format': 'RGB888','size':(3280,2464)})
cam.configure(camera_config)
cam.start()

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
print('\nArduino Connection Established')
pin_numbers = [3,5,6,9,10,11]
pin = {
0 : board.get_pin('d:3:p'),
1 : board.get_pin('d:5:p'),
2 : board.get_pin('d:6:p'),
3 : board.get_pin('d:9:p'),
4 : board.get_pin('d:10:p'),
5 : board.get_pin('d:11:p')
}

model = YOLO('yolov8n.onnx',task='detect')   # Loadigng required model

cv2.namedWindow("Inference", cv2.WINDOW_NORMAL)

# Loop through the video frames
while True:
    start_time = time.time()  # Start time measurement before inference

    image = cam.capture_array()

    results = next(model(image, stream=True, imgsz=256))

    inference_time = time.time() - start_time  # Calculate inference time
    
    annotated_frame = results.plot()
    cv2.imshow("Inference", annotated_frame)
    
    objs = ''
    for r in results:
        obj = r.names[int(r.boxes.cls[0].item())]
        cords = r.boxes.xyxyn.tolist()[0]
        x1,y1,x2,y2 = cords
        x = (x1+y1)/2
        y = (y1+y2)/2
        
        x0 = int(x/0.34)
        y0 = int(y/0.51)
        section = x0 + (y0*3)

        pin[section].write(0.9)
        os.system('echo "{0}" | festival --tts'.format(obj))
        pin[section].write(0)

    

    #print("fps:", 1/inference_time)  # Print the inference time
    #cv2.imshow("Inference", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        board.exit()
        break
        


cv2.destroyAllWindows()
