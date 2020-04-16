from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

while True:
    # --- Getting frames and drawing
    if kinect.has_new_color_frame():
        
        frame = kinect.get_last_color_frame()
        
        colourframe = np.reshape(frame, (2073600, 4))
        colourframe = colourframe[:,0:3]
        
        #extract then combine the RBG data
        colourframeR = colourframe[:,0]
        colourframeR = np.reshape(colourframeR, (1080, 1920))
        colourframeG = colourframe[:,1]
        colourframeG = np.reshape(colourframeG, (1080, 1920))        
        colourframeB = colourframe[:,2]
        colourframeB = np.reshape(colourframeB, (1080, 1920))
        
        framefullcolour = cv2.merge([colourframeR, colourframeG, colourframeB])
        
        cv2.imshow('Recording KINECT Video Stream', framefullcolour)
        
        frame = None
            
    key = cv2.waitKey(1)
    if key == 27: break