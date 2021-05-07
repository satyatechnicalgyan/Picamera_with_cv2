import io
import time
import picamera
import cv2
import numpy as np

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# Construct a numpy array from the stream
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
# "Decode" the image from the array, preserving colour
image = cv2.imdecode(data, 1)
# OpenCV returns an array with data in BGR order. If you want RGB instead
# use the following...
image = image[:, :, ::-1]

###################################################################################################################
#################trial2############################################################################################
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
#############
* PiCamera *
camera = PiCamera(framerate = 40)
time.sleep(2)
camera.resolution = (640,480)
rawCapture = PiRGBArray(camera, size=camera.resolution)
start = time.time()
for frame, i in zip(camera.capture_continuous(rawCapture, format="bgr", use_video_port=True), range(400)):
    image = frame.array
    rawCapture.truncate(0)
    ####################
    I am trying to process frames from my V2 RPI Camera at high framerates and am stuck with the picamera module. The VideoCapture class from OpenCV seems to be much faster than using PiCamera.capture_continuous(). Here are my two different test codes:

from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
* PiCamera *
camera = PiCamera(framerate = 40)
time.sleep(2)
camera.resolution = (640,480)
rawCapture = PiRGBArray(camera, size=camera.resolution)
start = time.time()
for frame, i in zip(camera.capture_continuous(rawCapture, format="bgr", use_video_port=True), range(400)):
    image = frame.array
    rawCapture.truncate(0)
print("Time for {0} frames: {1} seconds".format(frames ,time.time()-start))
* OpenCV *
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FPS, 40)
start = time.time()
for i in range(400):
    ret, img = cap.read()
print("Time for {0} frames: {1} seconds".format(frames, time.time() - start))
print("Time for {0} frames: {1} seconds".format(frames ,time.time()-start))
