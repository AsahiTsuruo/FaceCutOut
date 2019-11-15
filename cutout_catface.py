
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
def detect(imagefilename, cascadefilename):
    src_image = cv2.imread(imagefilename)
    srcimg = cv2.cvtColor(src_image,cv2.COLOR_RGB2GRAY)
    if srcimg is None:
        print("cannot load image")
        sys.exit(-1)
    dst_image = srcimg.copy()
    cascade = cv2.CascadeClassifier(cascadefilename)
    if cascade.empty():
        print("cannnot load cascade file")
        sys.exit(-1)
    objects = cascade.detectMultiScale(srcimg, 1.8, 7)
    print(objects,len(objects))
    if len(objects) >= 1:
        dst_image = dst_image[objects[0,1]:objects[0,1]+objects[0,3],objects[0,0]:objects[0,0]+objects[0,2]]
        return dst_image,1
    else:
        return dst_image,0
    

if __name__ == "__main__":
    image_num = 0
    for i in range(12500):
        input_image_dir = "./input/train/cat." + str(i)+".jpg"
        output_image_dir = "./output/train_cat/cat." + str(image_num)+".jpg"
        #input_image_dir = "./input/train/dog." + str(i)+".jpg"
        #output_image_dir = "./output/train_dog/dog." + str(image_num)+".jpg"
        result,flag = detect(input_image_dir, "haarcascade_frontalcatface.xml")
        if flag == 1:
            cv2.imwrite(output_image_dir, result)
            image_num = image_num + 1