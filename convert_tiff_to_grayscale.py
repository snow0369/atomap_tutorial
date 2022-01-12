import cv2
import os


def convert_tiff_to_grayscale(filename):
    sp = filename.split('.')
    new_filename = ".".join(sp[:-1]) + "_GS." + sp[-1]
    if not os.path.isfile(new_filename):
        img = cv2.imread(filename)
        cv2.imwrite(new_filename, img[:, :, 1])
    return new_filename
