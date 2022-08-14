import PIL
import numpy as np
import cv2

def image_process(img, args):
    img.thumbnail(args.max_size)
    # to numpy
    img = np.asarray(img)
    return image_binarize(img[:, :, 0], args)

def image_binarize(img, args):
    # binarize
    if args.type_binarize == "my":
        img_binary = (img > np.quantile(img.flatten(), 0.4)).astype(np.uint8)
    elif args.type_binarize == "binary":
        _, img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img_binary = img_binary // 255
    elif args.type_binarize == "mean":
        img_binary = cv2.adaptiveThreshold(
            img, 255, 
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 
            args.window_size[0], args.window_size[1]
        ) // 255
    elif args.type_binarize == "gaussian":
        img_binary = cv2.adaptiveThreshold(
            img, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 
            args.window_size[0], args.window_size[1]
        ) // 255
    else:
        print("Wrong type of binarization!")
        return
    
    return img_binary