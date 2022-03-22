from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
file_name = 'ScreenRecording'+ timestamp +'.mp4'
fource = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter(file_name,fource,20.0,(width,height))

print(width,height)

while True:
    image = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(image)
    image_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', image_final)
    captured_video.write(image_final)
    if cv2.waitKey(10) == ord('q'):
        break