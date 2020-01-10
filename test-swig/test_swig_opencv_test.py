#!/usr/bin/python2.7

import cv2
import test_swig_opencv

img = cv2.imread("test_swig_opencv.jpg")

o = test_swig_opencv.UsefulStuffUsingOpenCV()
o.doit(img)

cv2.namedWindow("test", flags=cv2.WINDOW_NORMAL)
cv2.imshow("test", img)
cv2.waitKey(0)
