import numpy as np
import argparse
import cv2
from math import *
def rotate(image, angle, center=None, scale=1.0):

    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


def rotateKeepAll(image, angle, center=None):

    (height, width) = image.shape[:2]
    heightNew=int(width*fabs(sin(radians(angle)))+height*fabs(cos(radians(angle))))
    widthNew=int(height*fabs(sin(radians(angle)))+width*fabs(cos(radians(angle))))
    if center is None:
        center = (width / 2, height / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    M[0,2]+=(widthNew-width)/2
    M[1,2]+=(heightNew-height)/2
    rotated = cv2.warpAffine(image, M, (widthNew, heightNew))

    return rotated

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"],0)
cv2.imshow("Original", image)

rotated = rotateKeepAll(image, 45)
cv2.imshow("Rotated by 45 Degrees keepall", rotated)
rotated = rotate(image, 45,scale=2.0)
cv2.imshow("Rotated by 45 Degrees 2.0", rotated)
cv2.waitKey(0)