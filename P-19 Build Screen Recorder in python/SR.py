import cv2
import pyautogui
from win32api import GetSystemMetrics #fro  is used when we need a function
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1) #when we give 0 or 1 it captures the whole screen

dim = (width,height)

#now we need varible to tell the python in whivh format we want to make the video
f = cv2.VideoWriter_fourcc(*"XVID") #for XVID it will give mp4 ectc format

output = cv2.VideoWriter("SR.mp4",f,30.0,dim) #giving the location in standard 30.0 frames per second is capture in a frame

now_start_time = time.time()

dur = 10+4 #suppose we have 10 sec then when the code is compiles 4 sec will be taken so 4 sec is added

#we will give start time and then the end time
end_time = now_start_time + dur 

while True:
    image = pyautogui.screenshot()
    #create a framd and add the screen shots in that frame
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)

    c_time = time.time()

    #now stop the capturing
    if c_time>end_time:
        break

#realease the video
output.release()

print("---END---")