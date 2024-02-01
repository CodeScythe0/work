# Using Machine Learning to aid the specially abled
The aim was to create a smart walking stick for people who are blind that would be able to use an ML model to detect objects in the immediate surroundings and provide audio and other stimuli to aid in sensing the environment.
We used :
- Raspberry Pi 4 model b
- Raspberry Pi Camera module v2
- Arduino Nano
- Button sized Vibraton motors
- A walking stick
- Power bank

Software Components:
- Entire code was written in python, even the arduino borad was controlled using Pyfirmatta
- We used YOLOv8 in nano size, exported in onnx format, to improve performance on CPU

Possible Improvemnts:

We planned to do distance approximation using LiDar and fine-tuning the vibration to convey the distance info, but that plan had some setbacks. 
GPS integration was to be performed to implement Google Maps API. 
A major change would be, to replace the Raspberry Pi with the user's mobile phone, so the raspberry pi 4, camera module and the power band will be replaced. And an app can be made to perform image processing.
