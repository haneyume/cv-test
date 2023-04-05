# coding:utf-8

import numpy as np
import cv2
import os


file_path = os.path.join(os.getcwd(), 'scripts/res/lena.png')
print(file_path)

img = cv2.imread(file_path)

cv2.imshow('image', img)

key = cv2.waitKey(0)

if key == 32:
    cv2.destroyAllWindows()
