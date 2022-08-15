import os
import cv2
from image_to_braille import ImageToBraille
from image_processing import image_process
from copy import deepcopy
from PIL import Image
import time

from multiprocessing import Process
from playsound import playsound
import signal

is_running = True
def handler(signum, frame):
    global is_running
    is_running = False

signal.signal(signal.SIGINT, handler)


class VideoPlayer():
    def __init__(self, args):
        self.args = deepcopy(args)
        self.AUDIO_NAME = 'tmp_audio.mp3'

    def play_video(self):
        cap = cv2.VideoCapture(self.args.path)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        time_start = time.time()
        curr_frame_number = 0
        while cap.isOpened() and is_running:
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
            else:
                continue
            
            img = image_process(Image.fromarray(frame), self.args)
            ImageToBraille(img).show()
            # print(time.time() - time_start)
        cap.release()

    def play_audio(self):
        playsound(self.audio_path)

    def create_autio(self):
        dirname = os.path.dirname(self.args.path)
        self.audio_path = os.path.join(dirname, self.AUDIO_NAME)
        os.system(f"ffmpeg -i {self.args.path} {self.audio_path}")
    
    def play(self):
        if self.args.audio:
            print('creating audio...')
            self.create_autio()
            time.sleep(0.5)
            print('done!')

            p = Process(target=self.play_audio)
            p.start()
            self.play_video()
            if p.is_alive():
                p.terminate()
                p.join()
            p.close()
        else:
            self.play_video()