# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
def transfer_color2gray(imagefilename):
    src_image = cv2.imread(imagefilename)
    srcimg = cv2.cvtColor(src_image,cv2.COLOR_RGB2GRAY)
    return srcimg

if __name__ == "__main__":
    for i in range(374):
        input_image_dir = "./input/train_dog/color/dog." + str(i)+".png"
        output_image_dir = "./output/train_dog/dog." + str(i)+".jpg"
        result = transfer_color2gray(input_image_dir)
        cv2.imwrite(output_image_dir, result)