import os
import cv2
from image_to_braille import ImageToBraille
from image_processing import image_process
from copy import deepcopy
from PIL import Image
import time


class VideoPlayer():
    def __init__(self, args):
        self.args = deepcopy(args)
    
    def play(self):
        
        time_start = time.time()
        while time.time() - time_start < 2:
            print(time.time()-time_start)

        cap = cv2.VideoCapture(self.args.path)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        time_start = time.time()
        curr_frame_number = 0
        while cap.isOpened():
            os.system('clear')

            ret, frame = cap.read()
            curr_frame_number += 1
            
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            
            curr_timedelta = time.time() - time_start
            
            diff = curr_frame_number / fps - curr_timedelta
            if diff > 0:
                time.sleep(diff)
            
            img = image_process(Image.fromarray(frame), self.args)
            ImageToBraille(img).show()
            print(curr_frame_number / fps)
            # print(time.time() - time_start)

        cap.release()
