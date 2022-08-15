from PIL import Image
import numpy as np
import argparse

from image_to_braille import ImageToBraille
from image_processing import image_process
from video_play import VideoPlayer


def main():
    parser = argparse.ArgumentParser(
        description="Hello! This is a script to view images in terminal.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-p", dest="path", type=str, required=True, help="path to image")
    parser.add_argument("--max_size", dest="max_size", default=[300, 300], action='store', type=int, help='max size of the image', nargs=2)
    parser.add_argument("--type_binarize", dest="type_binarize", default="binary", type=str,
        help="there are 4 options: \n\
            - my: choice threshold constant for all the pic, \n\
            - binary: choice threshold constant for all the pic, \n\
            - mean: choice threshold constant for specific window, \n\
            - gaussian: choice threshold constant for specific window, \n\
        for more information: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html")
    parser.add_argument(
        "--window_size", dest="window_size", 
        default=[7, 7], action="store", 
        type=int, help='size of the specific window', nargs=2)
    parser.add_argument(
        "--type", dest="type", type=str, help='there are 2 options: \n\
            video: if you want to play the video, \n\
            picture: if you want to see the picture. \n', default='picture')

    parser.add_argument('--audio', dest='audio', action='store_true', help='you want audio in video')
    parser.add_argument('--no-audio', dest='audio', action='store_false', help="you don't want audio in video(default)")
    parser.set_defaults(audio=False)

    args = parser.parse_args()

    if args.type == 'picture':
        img = Image.open(args.path)
        img_binary = image_process(img, args)
        
        # print the image
        ImageToBraille(img_binary).show()
    elif args.type == 'video':
        player = VideoPlayer(args)
        player.play()
    
if __name__ == "__main__":
    main()
