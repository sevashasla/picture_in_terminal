from PIL import Image
import numpy as np
from image_to_brailer import ImageToBrailer
import argparse
import cv2

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
    args = parser.parse_args()

    img = Image.open(args.path)
    img.thumbnail(args.max_size)

    # to numpy
    img = np.asarray(img)
    
    # binarize
    if args.type_binarize == "my":
        img_binary = (img[:, :, 0] > np.quantile(img[:, :, 0].flatten(), 0.4)).astype(np.uint8)
    elif args.type_binarize == "binary":
        _, img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img_binary = img_binary[:, :, 0] // 255
    elif args.type_binarize == "mean":
        img_binary = cv2.adaptiveThreshold(
            img[:, :, 0], 255, 
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 
            args.window_size[0], args.window_size[1]
        ) // 255
    elif args.type_binarize == "gaussian":
        img_binary = cv2.adaptiveThreshold(
            img[:, :, 0], 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 
            args.window_size[0], args.window_size[1]
        ) // 255
    else:
        print("Wrong type of binarization!")
        return
    
    # print the image
    ImageToBrailer(img_binary).show()
    
if __name__ == "__main__":
    main()
